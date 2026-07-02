# --- Do not remove these libs ---
from freqtrade.strategy.interface import IStrategy
from pandas import DataFrame
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
import pandas as pd  # noqa
pd.options.mode.chained_assignment = None  # default='warn'
import technical.indicators as ftt
from functools import reduce
from datetime import datetime, timedelta
from freqtrade.strategy import merge_informative_pair
from freqtrade.strategy import IntParameter, DecimalParameter, CategoricalParameter
import numpy as np
from freqtrade.strategy import stoploss_from_open


class ichiV1_futures(IStrategy):
    """
    Futures-capable variant of ichiV1 that trades both long and short.

    The short side is the exact mirror image of the long side:
      * price below the Ichimoku cloud instead of above it,
      * bearish (trend_close < trend_open) instead of bullish trends,
      * the fan contracting (fan_magnitude < 1 and shrinking) instead of expanding,
      * exit on a bullish cross instead of a bearish cross.

    All long and short parameters are hyperoptable.
    """

    INTERFACE_VERSION = 3

    # Allow this strategy to open short positions (requires futures trading).
    can_short = True

    # All trend_close_* columns, used as choices for the exit trend indicators.
    _trend_indicators = [
        "trend_close_5m", "trend_close_15m", "trend_close_30m", "trend_close_1h",
        "trend_close_2h", "trend_close_4h", "trend_close_6h", "trend_close_8h",
    ]

    # --- Hyperoptable LONG parameters --------------------------------------- #
    # NOTE: defaults are the original ichiV1 settings (25th july 21).
    buy_trend_above_senkou_level = IntParameter(1, 8, default=1, space="buy", optimize=True)
    buy_trend_bullish_level = IntParameter(1, 8, default=2, space="buy", optimize=True)
    buy_fan_magnitude_shift_value = IntParameter(1, 10, default=1, space="buy", optimize=True)
    buy_min_fan_magnitude_gain = DecimalParameter(
        1.0, 1.01, default=1.001, decimals=3, space="buy", optimize=True
    )

    # --- Hyperoptable SHORT parameters (mirror image of the long params) ----- #
    short_trend_below_senkou_level = IntParameter(1, 8, default=1, space="buy", optimize=True)
    short_trend_bearish_level = IntParameter(1, 8, default=2, space="buy", optimize=True)
    short_fan_magnitude_shift_value = IntParameter(1, 10, default=1, space="buy", optimize=True)
    short_max_fan_magnitude_gain = DecimalParameter(
        0.99, 1.0, default=0.999, decimals=3, space="buy", optimize=True
    )

    # --- Hyperoptable EXIT parameters --------------------------------------- #
    sell_trend_indicator = CategoricalParameter(
        _trend_indicators, default="trend_close_2h", space="sell", optimize=True
    )
    exit_short_trend_indicator = CategoricalParameter(
        _trend_indicators, default="trend_close_2h", space="sell", optimize=True
    )

    # ROI table:
    minimal_roi = {
        "0": 0.059,
        "10": 0.037,
        "41": 0.012,
        "114": 0
    }

    # Stoploss:
    # NOTE: was -0.275 (-27.5%), which is unrealistic on leveraged futures and
    # mechanically inflates the win rate (tiny ROI target + huge stop => almost
    # every trade hits ROI before the stop). Set to a realistic -5% to reveal the
    # true edge. Hyperopt the stoploss space to refine.
    stoploss = -0.05

    # Optimal timeframe for the strategy
    timeframe = '5m'

    # 400 candles needed so the long EMAs (EMA-96 = trend_close_8h) and the
    # Ichimoku senkou_b (window 120 + displacement 30 = 150) are fully converged.
    # recursive-analysis shows the variance drops to 0.000% at ~399 startup candles
    # (vs. 0.123% at 96), so backtest and live values match.
    startup_candle_count = 400
    process_only_new_candles = False

    trailing_stop = False
    #trailing_stop_positive = 0.002
    #trailing_stop_positive_offset = 0.025
    #trailing_only_offset_is_reached = True

    use_exit_signal = True
    exit_profit_only = False
    ignore_roi_if_entry_signal = False

    # Leverage used for futures trading. Override in the config if needed.
    leverage_value = 1.0

    # --- Position sizing --------------------------------------------------- #
    # Each trade uses a fixed fraction of the wallet as MARGIN (collateral).
    # With isolated margin and leverage L, the position notional = margin * L,
    # so leverage amplifies the exposure (and the gains/losses), while the
    # worst-case loss per trade is capped at the margin by isolated liquidation
    # (i.e. at most `margin_per_trade` of the wallet).
    # Set use_custom_sizing = False to fall back to Freqtrade's default sizing.
    use_custom_sizing = True
    margin_per_trade = 0.01  # 1% of the wallet as margin per trade

    plot_config = {
        'main_plot': {
            # fill area between senkou_a and senkou_b
            'senkou_a': {
                'color': 'green', #optional
                'fill_to': 'senkou_b',
                'fill_label': 'Ichimoku Cloud', #optional
                'fill_color': 'rgba(255,76,46,0.2)', #optional
            },
            # plot senkou_b, too. Not only the area to it.
            'senkou_b': {},
            'trend_close_5m': {'color': '#FF5733'},
            'trend_close_15m': {'color': '#FF8333'},
            'trend_close_30m': {'color': '#FFB533'},
            'trend_close_1h': {'color': '#FFE633'},
            'trend_close_2h': {'color': '#E3FF33'},
            'trend_close_4h': {'color': '#C4FF33'},
            'trend_close_6h': {'color': '#61FF33'},
            'trend_close_8h': {'color': '#33FF7D'}
        },
        'subplots': {
            'fan_magnitude': {
                'fan_magnitude': {}
            },
            'fan_magnitude_gain': {
                'fan_magnitude_gain': {}
            }
        }
    }

    def leverage(
        self,
        pair: str,
        current_time: datetime,
        current_rate: float,
        proposed_leverage: float,
        max_leverage: float,
        entry_tag,
        side: str,
        **kwargs,
    ) -> float:
        """
        Return the leverage to use for a new trade. Capped at the exchange
        maximum so the strategy stays valid across pairs.

        Reads ``leverage_value`` from the config at runtime (falls back to the
        class default), so it can be changed live via FreqUI's "Reload Config".
        """
        leverage_value = self.config.get("leverage_value", self.leverage_value)
        return min(leverage_value, max_leverage)

    def custom_stake_amount(
        self,
        pair: str,
        current_time: datetime,
        current_rate: float,
        proposed_stake: float,
        min_stake,
        max_stake: float,
        leverage: float,
        entry_tag,
        side: str,
        **kwargs,
    ) -> float:
        """
        Fixed-fraction margin sizing.

        Each trade uses ``margin_per_trade`` of the wallet as MARGIN (the stake).
        Freqtrade multiplies this stake by the leverage (see ``leverage()``) to
        get the position notional, so e.g. 1% margin at 10x => 10% notional
        exposure. With isolated margin the worst-case loss per trade is bounded
        to the margin itself (= margin_per_trade of the wallet).

        Reads ``margin_per_trade`` from the config at runtime (falls back to the
        class default), so it can be changed live via FreqUI's "Reload Config".
        """
        if not self.use_custom_sizing:
            return proposed_stake

        wallet = self.wallets.get_total_stake_amount()
        if not wallet:
            return proposed_stake

        margin_per_trade = self.config.get("margin_per_trade", self.margin_per_trade)
        stake = wallet * margin_per_trade

        if min_stake:
            stake = max(stake, min_stake)
        return min(stake, max_stake)

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        heikinashi = qtpylib.heikinashi(dataframe)
        dataframe['open'] = heikinashi['open']
        #dataframe['close'] = heikinashi['close']
        dataframe['high'] = heikinashi['high']
        dataframe['low'] = heikinashi['low']

        dataframe['trend_close_5m'] = dataframe['close']
        dataframe['trend_close_15m'] = ta.EMA(dataframe['close'], timeperiod=3)
        dataframe['trend_close_30m'] = ta.EMA(dataframe['close'], timeperiod=6)
        dataframe['trend_close_1h'] = ta.EMA(dataframe['close'], timeperiod=12)
        dataframe['trend_close_2h'] = ta.EMA(dataframe['close'], timeperiod=24)
        dataframe['trend_close_4h'] = ta.EMA(dataframe['close'], timeperiod=48)
        dataframe['trend_close_6h'] = ta.EMA(dataframe['close'], timeperiod=72)
        dataframe['trend_close_8h'] = ta.EMA(dataframe['close'], timeperiod=96)

        dataframe['trend_open_5m'] = dataframe['open']
        dataframe['trend_open_15m'] = ta.EMA(dataframe['open'], timeperiod=3)
        dataframe['trend_open_30m'] = ta.EMA(dataframe['open'], timeperiod=6)
        dataframe['trend_open_1h'] = ta.EMA(dataframe['open'], timeperiod=12)
        dataframe['trend_open_2h'] = ta.EMA(dataframe['open'], timeperiod=24)
        dataframe['trend_open_4h'] = ta.EMA(dataframe['open'], timeperiod=48)
        dataframe['trend_open_6h'] = ta.EMA(dataframe['open'], timeperiod=72)
        dataframe['trend_open_8h'] = ta.EMA(dataframe['open'], timeperiod=96)

        dataframe['fan_magnitude'] = (dataframe['trend_close_1h'] / dataframe['trend_close_8h'])
        dataframe['fan_magnitude_gain'] = dataframe['fan_magnitude'] / dataframe['fan_magnitude'].shift(1)

        ichimoku = ftt.ichimoku(dataframe, conversion_line_period=20, base_line_periods=60, laggin_span=120, displacement=30)
        # NOTE: 'chikou_span' (close.shift(-displacement)) looks 'displacement' candles
        # into the FUTURE and introduces look-ahead bias. It is not used in any entry/exit
        # condition, so we deliberately do not add it to the dataframe.
        dataframe['tenkan_sen'] = ichimoku['tenkan_sen']
        dataframe['kijun_sen'] = ichimoku['kijun_sen']
        dataframe['senkou_a'] = ichimoku['senkou_span_a']
        dataframe['senkou_b'] = ichimoku['senkou_span_b']
        dataframe['leading_senkou_span_a'] = ichimoku['leading_senkou_span_a']
        dataframe['leading_senkou_span_b'] = ichimoku['leading_senkou_span_b']
        dataframe['cloud_green'] = ichimoku['cloud_green']
        dataframe['cloud_red'] = ichimoku['cloud_red']

        dataframe['atr'] = ta.ATR(dataframe)

        return dataframe


    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        # ------------------------------------------------------------------ #
        # LONG entries
        # ------------------------------------------------------------------ #
        conditions = []

        # Trending market
        if self.buy_trend_above_senkou_level.value >= 1:
            conditions.append(dataframe['trend_close_5m'] > dataframe['senkou_a'])
            conditions.append(dataframe['trend_close_5m'] > dataframe['senkou_b'])

        if self.buy_trend_above_senkou_level.value >= 2:
            conditions.append(dataframe['trend_close_15m'] > dataframe['senkou_a'])
            conditions.append(dataframe['trend_close_15m'] > dataframe['senkou_b'])

        if self.buy_trend_above_senkou_level.value >= 3:
            conditions.append(dataframe['trend_close_30m'] > dataframe['senkou_a'])
            conditions.append(dataframe['trend_close_30m'] > dataframe['senkou_b'])

        if self.buy_trend_above_senkou_level.value >= 4:
            conditions.append(dataframe['trend_close_1h'] > dataframe['senkou_a'])
            conditions.append(dataframe['trend_close_1h'] > dataframe['senkou_b'])

        if self.buy_trend_above_senkou_level.value >= 5:
            conditions.append(dataframe['trend_close_2h'] > dataframe['senkou_a'])
            conditions.append(dataframe['trend_close_2h'] > dataframe['senkou_b'])

        if self.buy_trend_above_senkou_level.value >= 6:
            conditions.append(dataframe['trend_close_4h'] > dataframe['senkou_a'])
            conditions.append(dataframe['trend_close_4h'] > dataframe['senkou_b'])

        if self.buy_trend_above_senkou_level.value >= 7:
            conditions.append(dataframe['trend_close_6h'] > dataframe['senkou_a'])
            conditions.append(dataframe['trend_close_6h'] > dataframe['senkou_b'])

        if self.buy_trend_above_senkou_level.value >= 8:
            conditions.append(dataframe['trend_close_8h'] > dataframe['senkou_a'])
            conditions.append(dataframe['trend_close_8h'] > dataframe['senkou_b'])

        # Trends bullish
        if self.buy_trend_bullish_level.value >= 1:
            conditions.append(dataframe['trend_close_5m'] > dataframe['trend_open_5m'])

        if self.buy_trend_bullish_level.value >= 2:
            conditions.append(dataframe['trend_close_15m'] > dataframe['trend_open_15m'])

        if self.buy_trend_bullish_level.value >= 3:
            conditions.append(dataframe['trend_close_30m'] > dataframe['trend_open_30m'])

        if self.buy_trend_bullish_level.value >= 4:
            conditions.append(dataframe['trend_close_1h'] > dataframe['trend_open_1h'])

        if self.buy_trend_bullish_level.value >= 5:
            conditions.append(dataframe['trend_close_2h'] > dataframe['trend_open_2h'])

        if self.buy_trend_bullish_level.value >= 6:
            conditions.append(dataframe['trend_close_4h'] > dataframe['trend_open_4h'])

        if self.buy_trend_bullish_level.value >= 7:
            conditions.append(dataframe['trend_close_6h'] > dataframe['trend_open_6h'])

        if self.buy_trend_bullish_level.value >= 8:
            conditions.append(dataframe['trend_close_8h'] > dataframe['trend_open_8h'])

        # Trends magnitude
        conditions.append(dataframe['fan_magnitude_gain'] >= self.buy_min_fan_magnitude_gain.value)
        conditions.append(dataframe['fan_magnitude'] > 1)

        for x in range(self.buy_fan_magnitude_shift_value.value):
            conditions.append(dataframe['fan_magnitude'].shift(x+1) < dataframe['fan_magnitude'])

        if conditions:
            dataframe.loc[
                reduce(lambda x, y: x & y, conditions),
                'enter_long'] = 1

        # ------------------------------------------------------------------ #
        # SHORT entries (mirror image of the long conditions)
        # ------------------------------------------------------------------ #
        short_conditions = []

        # Trending market (price below the cloud)
        if self.short_trend_below_senkou_level.value >= 1:
            short_conditions.append(dataframe['trend_close_5m'] < dataframe['senkou_a'])
            short_conditions.append(dataframe['trend_close_5m'] < dataframe['senkou_b'])

        if self.short_trend_below_senkou_level.value >= 2:
            short_conditions.append(dataframe['trend_close_15m'] < dataframe['senkou_a'])
            short_conditions.append(dataframe['trend_close_15m'] < dataframe['senkou_b'])

        if self.short_trend_below_senkou_level.value >= 3:
            short_conditions.append(dataframe['trend_close_30m'] < dataframe['senkou_a'])
            short_conditions.append(dataframe['trend_close_30m'] < dataframe['senkou_b'])

        if self.short_trend_below_senkou_level.value >= 4:
            short_conditions.append(dataframe['trend_close_1h'] < dataframe['senkou_a'])
            short_conditions.append(dataframe['trend_close_1h'] < dataframe['senkou_b'])

        if self.short_trend_below_senkou_level.value >= 5:
            short_conditions.append(dataframe['trend_close_2h'] < dataframe['senkou_a'])
            short_conditions.append(dataframe['trend_close_2h'] < dataframe['senkou_b'])

        if self.short_trend_below_senkou_level.value >= 6:
            short_conditions.append(dataframe['trend_close_4h'] < dataframe['senkou_a'])
            short_conditions.append(dataframe['trend_close_4h'] < dataframe['senkou_b'])

        if self.short_trend_below_senkou_level.value >= 7:
            short_conditions.append(dataframe['trend_close_6h'] < dataframe['senkou_a'])
            short_conditions.append(dataframe['trend_close_6h'] < dataframe['senkou_b'])

        if self.short_trend_below_senkou_level.value >= 8:
            short_conditions.append(dataframe['trend_close_8h'] < dataframe['senkou_a'])
            short_conditions.append(dataframe['trend_close_8h'] < dataframe['senkou_b'])

        # Trends bearish
        if self.short_trend_bearish_level.value >= 1:
            short_conditions.append(dataframe['trend_close_5m'] < dataframe['trend_open_5m'])

        if self.short_trend_bearish_level.value >= 2:
            short_conditions.append(dataframe['trend_close_15m'] < dataframe['trend_open_15m'])

        if self.short_trend_bearish_level.value >= 3:
            short_conditions.append(dataframe['trend_close_30m'] < dataframe['trend_open_30m'])

        if self.short_trend_bearish_level.value >= 4:
            short_conditions.append(dataframe['trend_close_1h'] < dataframe['trend_open_1h'])

        if self.short_trend_bearish_level.value >= 5:
            short_conditions.append(dataframe['trend_close_2h'] < dataframe['trend_open_2h'])

        if self.short_trend_bearish_level.value >= 6:
            short_conditions.append(dataframe['trend_close_4h'] < dataframe['trend_open_4h'])

        if self.short_trend_bearish_level.value >= 7:
            short_conditions.append(dataframe['trend_close_6h'] < dataframe['trend_open_6h'])

        if self.short_trend_bearish_level.value >= 8:
            short_conditions.append(dataframe['trend_close_8h'] < dataframe['trend_open_8h'])

        # Trends magnitude (fan contracting / below 1)
        short_conditions.append(dataframe['fan_magnitude_gain'] <= self.short_max_fan_magnitude_gain.value)
        short_conditions.append(dataframe['fan_magnitude'] < 1)

        for x in range(self.short_fan_magnitude_shift_value.value):
            short_conditions.append(dataframe['fan_magnitude'].shift(x+1) > dataframe['fan_magnitude'])

        if short_conditions:
            dataframe.loc[
                reduce(lambda x, y: x & y, short_conditions),
                'enter_short'] = 1

        return dataframe


    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        # LONG exit: trend_close crosses below the chosen trend indicator
        conditions = []
        conditions.append(qtpylib.crossed_below(dataframe['trend_close_5m'], dataframe[self.sell_trend_indicator.value]))

        if conditions:
            dataframe.loc[
                reduce(lambda x, y: x & y, conditions),
                'exit_long'] = 1

        # SHORT exit (mirror): trend_close crosses above the chosen trend indicator
        short_conditions = []
        short_conditions.append(qtpylib.crossed_above(dataframe['trend_close_5m'], dataframe[self.exit_short_trend_indicator.value]))

        if short_conditions:
            dataframe.loc[
                reduce(lambda x, y: x & y, short_conditions),
                'exit_short'] = 1

        return dataframe
