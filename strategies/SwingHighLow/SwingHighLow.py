# pragma pylint: disable=missing-docstring, invalid-name, pointless-string-statement

# --- Do not remove these libs ---
import numpy as np  # noqa
import pandas as pd  # noqa
from pandas import DataFrame

from freqtrade.strategy.interface import IStrategy

# --------------------------------
# Add your lib to import here
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib


class SwingHighLow(IStrategy):
    """
    Futures-capable variant of SwingHigh that trades both long and short.

    The short side mirrors the long logic: where the long side buys on a
    bullish MACD cross with an oversold CCI, the short side sells on a
    bearish MACD cross with an overbought CCI (and vice versa for exits).
    """

    INTERFACE_VERSION = 3

    # Allow this strategy to open short positions (requires futures trading).
    can_short = True

    # Disable ROI
    # Could be replaced with new ROI from hyperopt.
    minimal_roi = {"0": 0.16035, "23": 0.03218, "54": 0.01182, "173": 0}

    stoploss = -0.22274

    ### Do extra hyperopt for trailing seperat. Use "--spaces default" and then "--spaces trailing".
    ### See here for more information: https://www.freqtrade.io/en/latest/hyperopt
    trailing_stop = True
    trailing_stop_positive = 0.08
    trailing_stop_positive_offset = 0.10
    trailing_only_offset_is_reached = True

    timeframe = "30m"

    # Leverage used for futures trading. Override in the config if needed.
    leverage_value = 1.0

    def informative_pairs(self):
        return []

    def leverage(
        self,
        pair: str,
        current_time,
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
        """
        return min(self.leverage_value, max_leverage)

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        macd = ta.MACD(dataframe)
        dataframe["macd"] = macd["macd"]
        dataframe["macdsignal"] = macd["macdsignal"]

        ### Add timeperiod from hyperopt (replace xx with value):
        ### "xx" must be replaced even before the first hyperopt is run,
        ### else "xx" would be a syntax error because it must be a Integer value.
        dataframe["cci-buy"] = ta.CCI(dataframe, timeperiod=13)
        dataframe["cci-sell"] = ta.CCI(dataframe, timeperiod=76)

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        dataframe.loc[
            (
                (dataframe["macd"] > dataframe["macdsignal"])
                & (dataframe["cci-buy"] <= -188.0)
                & (dataframe["volume"] > 0)
            ),
            "enter_long",
        ] = 1

        # Short entry mirrors the long entry: bearish MACD cross with an
        # overbought CCI instead of a bullish cross with an oversold CCI.
        dataframe.loc[
            (
                (dataframe["macd"] < dataframe["macdsignal"])
                & (dataframe["cci-buy"] >= 188.0)
                & (dataframe["volume"] > 0)
            ),
            "enter_short",
        ] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        dataframe.loc[
            (
                (dataframe["macd"] < dataframe["macdsignal"])
                & (dataframe["cci-sell"] >= 231.0)
                & (dataframe["volume"] > 0)
            ),
            "exit_long",
        ] = 1

        # Short exit mirrors the long exit: bullish MACD cross with an
        # oversold CCI instead of a bearish cross with an overbought CCI.
        dataframe.loc[
            (
                (dataframe["macd"] > dataframe["macdsignal"])
                & (dataframe["cci-sell"] <= -231.0)
                & (dataframe["volume"] > 0)
            ),
            "exit_short",
        ] = 1

        return dataframe
