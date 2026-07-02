# Freqtrade Strategies Repository

This repository is dedicated to sharing open-source trading strategies for the Freqtrade cryptocurrency trading bot. We encourage contributors to help keep these strategies up to date with the latest Freqtrade versions and to add new strategies to benefit the community.

## About Freqtrade

[Freqtrade](https://www.freqtrade.io/) is an open-source cryptocurrency trading bot that allows users to create, backtest, and execute trading strategies on various cryptocurrency exchanges.

## Getting Started

### Prerequisites

Before you start contributing to this project, ensure you have the following:

- [Freqtrade](https://www.freqtrade.io/) installed on your machine.
- Basic knowledge of Python and Freqtrade.
- Familiarity with version control using Git.

## Strategie-Katalog & Bewertung

Überblick über alle Strategien im Repo. Erstellt durch Code-Analyse jeder einzelnen Strategie (Indikatoren, Entry/Exit-Logik, ROI/Stop/Trailing, Timeframe).

**Bewertungsmethodik (1–10):** Die Bewertung ist eine **heuristische Experten­einschätzung des Profitabilitäts­potenzials** — *kein* Backtest pro Strategie. Sie gewichtet: (a) Plausibilität eines echten Edges, (b) Overfitting-Risiko (hyperopt-„Magic Numbers", absurde Schwellen), (c) Qualität der Exit-Logik (echtes Exit-Signal vs. reines ROI/Stop), (d) Track-Record des Archetyps in Krypto, (e) Regime-Abhängigkeit. Grobe Skala: **1–2** kaputt/Platzhalter · **3–4** naiver Standard-Indikator-Cross, in der Regel kein durabler Edge · **5–6** solide/strukturiert oder bekannte Community-Lineage, aber overfit-anfällig · **7–8** durchdacht mit Risikomanagement · **9–10** nachgewiesen robust (selten). Krypto-Realität: die große Mehrheit öffentlicher Indikator-Strategien liegt bei 2–4.

**Risiko** = Kapitalrisiko-Profil: tiefer/fehlender Stop, Hebel, „kein echter Exit" (Verlierer laufen bis Stop), enge ROI mit tiefem Stop (viele Mini-Gewinne, seltener großer Verlust) → höheres Risiko.

| Strategie | Funktionsweise | Timeframe | Risiko | Bewertung |
|---|---|---|---|---|
| ADXMomentum | ADX>25 + Momentum>0 + DI+>DI-; Long im Aufwärts-Momentum, Exit bei Gegen-Momentum. Winziges ROI (1%), sehr tiefer Stop (-25%). | 1h | Hoch | 3 |
| ADX_15M_USDT | Hyperoptete ADX/DI-Kreuzung; Entry DI+ kreuzt DI-, hyperoptete Schwellen + gestaffeltes ROI. | 15m | Hoch | 3 |
| ADX_15M_USDT2 | Wie oben, aber Exit-Schwellen absurd (adx>91) → praktisch nur ROI/Stop treibt Exits. Überangepasst. | 15m | Hoch | 2 |
| ASDTSRockwellTrading | Klassischer MACD: Long wenn MACD>0 & über Signal, Exit bei Signal-Kreuzung. Tiefer Stop (-30%). | 5m | Hoch | 3 |
| ActionZone | EMA-Regime (fastMA>slowMA & Preis>fastMA) auf Tageschart. Kein Stop (-100%), kein ROI. Reines Trendfolge-Halten. | 1d | Hoch | 4 |
| AdxSmas | ADX>25 als Trendfilter + SMA-Short/Long-Kreuzung. Standard-Trendfolge. | 1h | Mittel | 3 |
| AlligatorStrat | SMA-Kreuzung + MACD>0 & über Signal als Bestätigung; Exit bei Preis<SMA & MACD-Kreuzung. | 4h | Mittel | 3 |
| AlligatorStrategy | EMA-Ribbon (7>30>50>100>121>200) ausgerichtet + Stoch-RSI-Filter. Kein Stop/ROI aktiv. | 1h | Mittel | 3 |
| AlwaysBuy | Kauft immer (leere Entry-Bedingung). Test-/Benchmark-Strategie, kein Signal. | 5m | Hoch | 1 |
| Apollo11 | Mehrsignal: VW-MACD, EMA-Stack, Fib-/BB-Bänder kombiniert. Elaborierter als der Durchschnitt. | 15m | Mittel | 4 |
| AverageStrategy | Reine MA-Kreuzung (maShort/maMedium), Exit bei Gegenkreuzung. Simpelster Trendfolger. | 4h | Mittel | 3 |
| AwesomeMacd | MACD>0 + Awesome-Oscillator kreuzt Nulllinie. Zwei-Momentum-Bestätigung. | 1h | Mittel | 3 |
| BBMod1 | BB_RPB_TSL-Derivat: Indikator-Suite (RMI/CCI/SRSI, BB-Squeeze, Fisher, Heikin, viele Sub-Signale), hyperoptet. | 5m | Mittel | 5 |
| BBRSI | Mean-Reversion: close<unteres BB & RSI>25 (fast immer wahr → im Kern nur BB-Touch); Exit RSI>95 (fast nie) → ROI/Stop-getrieben. | 4h | Mittel | 3 |
| BBRSI2 | close<unteres BB & RSI>35; Exit RSI>75 & close>BB-Mitte. 1m-Scalp, Trailing an. | 1m | Hoch | 2 |
| BBRSI21 | close<unteres BB & RSI<21; Exit close>oberes BB & RSI>99 (nie) → ROI-getrieben. | 5m | Hoch | 2 |
| BBRSI3366 | RSI<33 Entry; Exit oberes BB & RSI>66. BB/RSI-Mean-Reversion, gestaffeltes ROI. | 5m | Mittel | 3 |
| BBRSI4cust | DI+-Filter + Low kreuzt unter unteres BB; Exit High kreuzt über BB-Mitte (+ custom Exit). | 15m | Mittel | 3 |
| BBRSINaiveStrategy | Das Freqtrade-Tutorial-Beispiel: RSI>25 & close<unteres BB; Exit RSI>70 & close>BB-Mitte. Lehr-Baseline. | 15m | Mittel | 2 |
| BBRSIOptim2020Strategy | Hyperoptete BB-SD-Band-Variante (close<BB-3sd), Exit BB-Mitte. Überangepasst auf 2020. | 5m | Mittel | 2 |
| BBRSIOptimStrategy | Hyperoptete BB-2sd + RS=12 Entry; Exit-Bedingung inkonsistent (RSI>96). Overfit. | 5m | Mittel | 2 |
| BBRSIOptimizedStrategy | Hyperoptete BB-3sd Entry, RSI-Exit. Wie Optim-Familie, überangepasst. | 5m | Mittel | 2 |
| BBRSIS | BB-Touch + SMA-Stack (5>75>200)-Trendfilter + Multi-TF-Resample-RSI. Etwas strukturierter. | 5m | Mittel | 3 |
| BBRSIStrategy | Wie BBRSI, auf 15m. BB-SD-Band + RSI-Mean-Reversion. | 15m | Mittel | 3 |
| BBRSITV | TradingView-Stil: EWO (Elliott-Wave-Oszillator) + RSI vs. MA-Basisband. Hyperoptet. | 5m | Mittel | 3 |
| BBRSIoriginal | close<unteres BB3; Exit RSI>75 & close>BB-Mitte. BB-Mean-Reversion, hyperoptet ROI. | 1h | Mittel | 3 |
| BBRSIv2 | RSI kreuzt >35 & close<unteres BB, ODER RSI<23 & TEMA-Bedingungen. Zwei-Wege-Entry. | 15m | Mittel | 3 |
| BB_RPB_TSL | Bekannte Community-Lineage (RPB + Trailing-SL): Multi-Signal (RMI/CCI/SRSI, BB-Delta/-Width, Keltner-Squeeze, Ichimoku), custom TSL. Ausgereift, aber overfit-anfällig. | 5m | Mittel | 6 |
| BB_RPB_TSL_2 | BB_RPB_TSL-Variante, Stop -15% statt aus, sonst gleiche Multi-Signal-Basis. | 3m | Mittel | 5 |
| BB_RPB_TSL_BI | BB_RPB_TSL für Binance-Isolated-Tuning; gleiche Signal-Suite. | 5m | Mittel | 5 |
| BB_RPB_TSL_BIV1 | Weitere BB_RPB_TSL-BI-Variante, identische Kernlogik, andere Parameter. | 5m | Mittel | 5 |
| BB_RPB_TSL_RNG | RPB-TSL + EMA-26/12-Trendfilter beim Dip-Entry, Exit über MA-Offset & RSI-Fast/Slow. Range-Erweiterung der Lineage. | 5m | Mittel | 5 |
| BB_RPB_TSL_RNG_2 | Variante von RNG, identische Kernlogik, andere Parameter. | 5m | Mittel | 5 |
| BB_RPB_TSL_RNG_TBS | RNG mit „TBS"-Tuning (Trailing-Buy/Sell), sonst gleiche Signalbasis. | 5m | Mittel | 5 |
| BB_RPB_TSL_RNG_TBS_GOLD | Wie TBS, aber echter Stop -4,9% statt -99% → deutlich besseres Risikoprofil dieser Lineage. | 5m | Mittel | 5 |
| BB_RPB_TSL_RNG_VWAP | RNG + VWAP-Filter; Stop aus (-99%), ROI aus. Dip-Buy mit VWAP-Kontext. | 5m | Hoch | 5 |
| BB_RPB_TSL_SMA_Tranz | RPB-TSL + NFI-artige „Protections" (EMA/SMA-200-Stacks, safe_dips, 1h-Multi-TF) + BB-Upper-Multi-Candle-Exit. Robusterer Trendfilter. | 5m | Mittel | 6 |
| BB_RPB_TSL_SMA_Tranz_TB_1_1_1 | Variante der SMA_Tranz mit protection-Listen-Logik; gleiche Kernidee. | 5m | Mittel | 5 |
| BB_RPB_TSL_SMA_Tranz_TB_MOD | SMA_Tranz + Keltner-Squeeze-Entry, modifizierte ROI-Staffel. | 5m | Mittel | 5 |
| BB_RPB_TSL_Tranz | RPB-TSL mit Trailing-Buy-Mechanik (verzögerter Entry im Abwärts-Retrace) + 1h-ROC/BB-Width-Filter. | 5m | Mittel | 5 |
| BB_RPB_TSL_c7c477d_20211030 | Datierter Snapshot der Lineage + BTC-Safe-Guard & Ichimoku-1h-Filter im Exit. | 5m | Mittel | 5 |
| BB_RPB_TSLmeneguzzo | Community-Variante (meneguzzo) der RPB-TSL, gleiche Signal-Suite. | 5m | Mittel | 5 |
| BB_RSI | BB-Lower-Touch + RSI>7 (quasi immer wahr); Exit BB-Upper + RSI>74. Trailing, moderater Stop. | 1h | Mittel | 3 |
| BB_Strategy04 | Kauf knapp unter unterem BB (mit Stop-basierter Untergrenze), Exit oberes BB. Reine BB-Mean-Reversion. | 1h | Mittel | 3 |
| BBands | Riesiger Indikator-Import, aber Entry nur „TEMA steigt" → praktisch unvollständig/trivial. | 1m | Hoch | 2 |
| BBandsRSI | Klassik: RSI<30 & close<unteres BB; Exit RSI>70. ROI „0":0 → nimmt jeden Mini-Gewinn. | 5m | Mittel | 3 |
| BBlower | RSI 4 Bars steigend & RSI<50 & TEMA kreuzt über unteres BB. Trailing. Etwas mehr Filter. | 5m | Mittel | 3 |
| Babico_SMA5xBBmid | EMA5 kreuzt BB-Mitte auf Tageschart, Exit bei Gegenkreuzung. Kein Stop/ROI. Simpel. | 1d | Mittel | 3 |
| Bandtastic | Hyperopt-Template: konfigurierbare RSI/MFI/EMA/Multi-BB-Band-Kombi. Populäre Optimierungs-Basis. | 15m | Mittel | 4 |
| BbRoi | Momentum-Long im oberen BB-Halbband + EMA-Trend-Ausrichtung (close>ema9>ema200). Trailing. | 15m | Mittel | 3 |
| BbandRsi | Klassiker: RSI<30 & close<unteres BB; Exit RSI>70. Tiefer Stop (-25%). | 1h | Mittel | 3 |
| BbandRsiRolling | Rolling-Min-RSI<37 & close<unteres BB; kein Exit-Signal (nur ROI/Stop). | 5m | Mittel | 3 |
| BcmbigzDevelop | NFI-artiger Dip-Buyer: EMA-Stacks + Dip-Schwellen + Volume-Pump-Filter, Exit BB-Mitte/-Upper. | 5m | Hoch | 4 |
| BcmbigzV1 | CMF<-0,435 & RSI<22 & Volume-Pump am EMA-200-Trend. Dip-Kauf in Panik. | 5m | Hoch | 4 |
| BigPete | Multi-Buy-Conditions (BB-Lower-Dip, RSI-1h, Volume-Pump), Trailing, ROI aus. NFI-Verwandtschaft. | 5m | Hoch | 4 |
| BigZ03 | BigZ-Lineage (BinClucMad-Vorfahr): Dip unter BB-Lower + EMA-200-Trend + RSI-1h; Exit BB-Mitte. Kein Stop (-99%). | 5m | Hoch | 4 |
| BigZ0307HO | BigZ03 hyperoptet (HO), BB-Upper-Multi-Candle-Exit. | 5m | Hoch | 3 |
| BigZ03HO | Hyperopt-Variante von BigZ03, gleiche Kernlogik. | 5m | Hoch | 3 |
| BigZ04 | BigZ03-Nachfolger, quasi identische Dip-Buy-Logik. Kein Stop. | 5m | Hoch | 4 |
| BigZ0407 | BigZ04 mit hyperopteten Condition-Werten + BB-Upper-Exit. | 5m | Hoch | 3 |
| BigZ0407HO | Hyperopt-Variante von BigZ0407. | 5m | Hoch | 3 |
| BigZ04HO | Hyperopt-Variante von BigZ04. | 5m | Hoch | 3 |
| BigZ04HO2 | Weitere Hyperopt-Variante von BigZ04. | 5m | Hoch | 3 |
| BigZ04_TSL3 | BigZ04 + Trailing-SL-Exit (MA-Offset), ROI aus. | 5m | Hoch | 4 |
| BigZ04_TSL4 | Wie TSL3, weitere TSL-Iteration. | 5m | Hoch | 4 |
| BigZ06 | BigZ-Panik-Dip (CMF<-0,435 & RSI<22 & Volume-Pump), Exit BB-Mitte. | 5m | Hoch | 4 |
| BigZ07 | Wie BigZ06, leicht andere Filter. | 5m | Hoch | 4 |
| BigZ07Next | BigZ07 + BB-Upper-Multi-Candle-Exit, ZEMA/MFI ergänzt. | 5m | Hoch | 4 |
| BigZ07Next2 | Variante von BigZ07Next, andere ROI-Staffel. | 5m | Hoch | 4 |
| BinClucMad | Bekannte Lineage (BinanceCluc + MadDog): BB-Lower-Dip + EMA-200-Trend + Volume-Filter; Exit BB-Mitte/-Upper. Kein Stop. | 5m | Hoch | 4 |
| BinClucMadDevelop | BinClucMad + EMA-Stacks & Dip-Schwellen. Dev-Iteration. | 5m | Hoch | 4 |
| BinClucMadSMADevelop | BinClucMad + EWO (Elliott-Wave-Osz.) & SMA-Offset-Entry/Exit. Trailing, echter Stop (-22,8%). | 5m | Hoch | 4 |
| BinClucMadV1 | BinClucMad-Variante: EMA-200-Trend + close<0,99·BB-Lower + Volume-Filter; Exit BB-Mitte/-Upper. Kein Stop. | 5m | Hoch | 4 |
| BinHV27 | „BinanceHold V27": SMA-Band + DI + RSI mit Trend-State-Flags (preparechangetrend etc.). Strukturierter Klassiker. Stop -50%. | 5m | Hoch | 4 |
| BinHV45 | Kanonischer BB-Lower-Spike-Buy-Scalper (bbdelta/closedelta/tail, Cluc-Ursprung). Sehr bekannt. Stop -5%, ROI 1,25%. | 1m | Mittel | 4 |
| BinHV45HO | Hyperopt-Variante von BinHV45, Stop -19%. | 1m | Mittel | 3 |
| BreakEven | Keine Entry-Logik, nur ROI-Staffel zum Break-Even-Test. Utility, keine echte Strategie. | 5m | Niedrig | 1 |
| BuyAllSellAllStrategy | Kauft/verkauft alles — Test-/Benchmark. Kein Signal. | 5m | Hoch | 1 |
| BuyOnly | RSI kreuzt >30 & open≤unteres BB & TEMA steigt. Kein Exit-Signal. Simpel. | 15m | Mittel | 2 |
| CBPete9 | Cluc/Pete BB-Lower-Dip + Volume-Pump/-Drop-Filter; Exit BB-Mitte. Trailing, kein Stop. | 5m | Hoch | 4 |
| CCIStrategy | Dual-CCI<-100 + CMF + MFI<25 + Multi-TF-Resample-Trend. Gut gefilterte Mean-Reversion, enger Stop (-2%). | 1m | Mittel | 3 |
| CMCWinner | Oversold-Reversal: CCI<-100 & MFI<20 & CMO<-50 (verzögert). | 15m | Mittel | 3 |
| Cci | Pur: CCI<-198 Entry, CCI>197 Exit. Extrem simple Mean-Reversion, tiefer Stop. | 1m | Mittel | 3 |
| Chandem | CMO kreuzt über 0 (Momentum-Long), Exit close kreuzt oberes BB. Trailing. | 5m | Mittel | 3 |
| Chandemtwo | Wie Chandem, mehr CMO-Bestätigungs-Bars + CMO<-35-Exit. | 5m | Mittel | 3 |
| Chispei | Momentum-Guard + fastMA>slowMA-Trendfolge auf 4h. | 4h | Mittel | 3 |
| Cluc4 | ClucBot: ROCR-1h-Filter + BB-Spike-Buy (bbdelta/tail); Exit close kreuzt BB-Mitte. Sehr enger Stop (-1%). | 1m | Mittel | 3 |
| Cluc4werk | Hyperopt-Variante („werk") von Cluc4, Trailing. | 1m | Mittel | 3 |
| Cluc5werk | Hyperopt-Cluc mit High/Close-fallend-Exit, Trailing. | 1m | Mittel | 3 |
| Cluc7werk | Cluc + Fisher-RSI-Filter & ema_slow, Trailing, enger Stop (-2%). | 1m | Mittel | 4 |
| ClucFiatROI | Cluc + Fisher-RSI + ema_slow + Entry/Exit-Timeout-Callbacks. Trailing. | 5m | Mittel | 4 |
| ClucFiatSlow | Wie ClucFiatROI, langsamere Timeout-Variante. | 5m | Mittel | 4 |
| ClucHAnix | Cluc auf Heikin-Ashi (ha_close) BB-Spike-Buy. Populär. Kein Stop, HA-fallend-Exit. | 1m | Hoch | 4 |
| ClucHAnix5m | ClucHAnix-5m-Port + Lambo/Anti-Pump/BTC-Safe (NFI-Elemente) & EWO. | 5m | Hoch | 4 |
| ClucHAnix_5m | ClucHAnix 5m, hyperoptbare Parameter + Fisher-Exit. | 5m | Hoch | 4 |
| ClucHAnix_5m1 | Wie _5m, weitere Parameter-Iteration. | 5m | Hoch | 4 |
| ClucHAnix_BB_RPB_MOD | ClucHA + RPB-Merge + Lambo + Anti-Pump + BTC-Safe. Elaborierter Dip-Buyer. | 1m | Hoch | 5 |
| ClucHAnix_BB_RPB_MOD2_ROI | Wie MOD, mit ROI-Staffel-Exit statt reinem HA-Signal. | 5m | Hoch | 5 |
| ClucHAnix_BB_RPB_MOD_CTT | MOD-Variante (CTT-Tuning), gleiche Kernlogik. | 5m | Hoch | 5 |
| ClucHAnix_BB_RPB_MOD_E0V1E_ROI | MOD-Variante (E0V1E), ROI-Exit. | 5m | Hoch | 5 |
| ClucHAnix_hhll | ClucHA + HMA/CMF & Higher-High/Lower-Low-Kontext, Fisher-Exit. | 5m | Hoch | 4 |
| ClucHAwerk | Hyperopt-Variante der ClucHA, Trailing, enger Stop (-2,1%). | 1m | Mittel | 4 |
| ClucMay72018 | Früher Cluc: close<ema100 & close<0,985·BB-Lower + Volume-Cap; Exit BB-Mitte. Stop -5%. | 5m | Mittel | 3 |
| CofiBitStrategy | Stoch-Fast-K/D-Kreuzung + open<ema_low + ADX-Filter. Scalp. | 5m | Mittel | 3 |
| CombinedBinHAndCluc | Bekannte Kombi BinH+Cluc BB-Spike-Buy + ema_slow-Filter; Exit BB-Mitte. Stop -5%. | 5m | Mittel | 4 |
| CombinedBinHAndCluc2021 | 2021-Update der Kombi, ema100-Filter, Stop -9%. | 5m | Mittel | 4 |
| CombinedBinHAndCluc2021Bull | Bull-Tuning der 2021-Kombi, gleiche Logik. | 5m | Mittel | 4 |
| CombinedBinHAndClucHyperV0 | Hyperoptbare, fenster-parametrisierte Kombi. Kein echter Exit (ROI aus). | 1m | Mittel | 3 |
| CombinedBinHAndClucHyperV3 | HyperV0 + ATR-basierte Sell-Rate, Stop -6%. | 1m | Mittel | 4 |
| CombinedBinHAndClucV2 | Kombi + Regime-Gate (go_long) & MFI/Stoch/ATR-Filter. 1h-Variante. | 1h | Mittel | 4 |
| CombinedBinHAndClucV3 | Kombi-Iteration, Trailing, kein Stop, BB-Upper-Multi-Candle-Exit. | 5m | Hoch | 4 |
| CombinedBinHAndClucV4 | Wie V3, leicht andere Exit-Bedingung. | 5m | Hoch | 4 |
| CombinedBinHAndClucV5 | Kombi V5, Trailing, kürzerer BB-Upper-Exit. | 5m | Hoch | 4 |
| CombinedBinHAndClucV5Hyperoptable | V5 mit hyperoptbaren Schwellen. | 5m | Hoch | 4 |
| CombinedBinHAndClucV6 | V6 + EMA-200-1h/EMA-50-Trendfilter vor dem Dip-Entry. Bestes Risikoprofil der Kombi-Reihe. | 5m | Hoch | 5 |
| CombinedBinHAndClucV6H | V6 hyperoptbar (Schwellen als Parameter), Trailing. | 5m | Hoch | 5 |
| CombinedBinHAndClucV7 | V6 + Dip-Schwellen (rolling-open-max) & BB40-Spike-Buy + RSI-Exit. | 5m | Hoch | 5 |
| CombinedBinHAndClucV8 | V7-Linie, ROI aus (10), 4-Candle-BB-Upper-Exit. | 5m | Hoch | 4 |
| CombinedBinHAndClucV8Hyper | V8 + hyperoptete ROI-Staffel. | 5m | Hoch | 4 |
| CombinedBinHAndClucV8XH | V8-Variante (XH-Tuning). | 5m | Hoch | 4 |
| CombinedBinHAndClucV8XHO | V8XH hyperoptet. | 5m | Hoch | 4 |
| CombinedBinHClucAndMADV3 | BinH+Cluc+MadDog: EMA-Trend + BB-Spike-Buy; Exit BB-Mitte. Kein Stop. | 5m | Hoch | 4 |
| CombinedBinHClucAndMADV5 | MAD-Merge: EMA-200-Trend + close<0,99·BB-Lower + Volume-Cap. | 5m | Hoch | 4 |
| CombinedBinHClucAndMADV6 | Wie V5 + Anti-Pump-Volume-Filter. | 5m | Hoch | 4 |
| CombinedBinHClucAndMADV9 | MAD-Merge mit Safe-Band-Faktor & Volume-Drop-Filter. | 5m | Hoch | 4 |
| Combined_Indicators | Cluc-BB-Spike-Buy + ema_slow-Filter; Exit BB-Mitte. Trailing, Stop -6,6%. | 1m | Mittel | 3 |
| Combined_NFIv6_SMA | NostalgiaForInfinity-Derivat (v6) + SMA-Offset: RSI-slow fallend + rsi_fast<35 + uptrend_1h + MA-Lower-Dip. Ernsthafte Lineage. Kein Stop, Trailing. | 5m | Hoch | 5 |
| Combined_NFIv7_SMA | NFI v7 + SMA-Offset, mehr Entry-Conditions & BB20-Exit. | 5m | Hoch | 5 |
| Combined_NFIv7_SMA_Rallipanos_20210707 | Community-getuntes NFIv7-Snapshot (Rallipanos). | 5m | Hoch | 5 |
| Combined_NFIv7_SMA_bAdBoY_20211204 | Community-getuntes NFIv7-Snapshot (bAdBoY). | 5m | Hoch | 5 |
| CoreStrategy | SMAOffset-Archetyp: close<MA·Offset + EWO + RSI (Elliott-Wave-Osz.); Exit MA-Cross/BB. Trailing. | 5m | Mittel | 4 |
| CrossEMAStrategy | EMA28>EMA48 + Stoch-RSI-Filter; Exit bei Gegenkreuzung. Kein Stop/ROI. | 1h | Mittel | 3 |
| CryptoFrog | Bekannte Multi-Indikator-Strat: Smoothed-Heikin-Ashi + BBW-Expansion/Squeeze + MFI + DMI + SAR + Stoch-RSI, dynamische ROI/Stop. Durchdacht. | 5m | Mittel | 5 |
| CryptoFrogHO | Hyperopt-Variante von CryptoFrog, Stop -13%. | 5m | Mittel | 4 |
| CryptoFrogHO2 | Weitere CryptoFrog-Hyperopt-Iteration. | 5m | Mittel | 4 |
| CryptoFrogHO2A | CryptoFrog-HO2-Variante. | 5m | Mittel | 4 |
| CryptoFrogHO3A1 | CryptoFrog-HO3-Serie (andere ROI/Stop-Kombis), overfit-anfällig. | 5m | Mittel | 4 |
| CryptoFrogHO3A2 | CryptoFrog-HO3-Variante. | 5m | Mittel | 4 |
| CryptoFrogHO3A3 | CryptoFrog-HO3-Variante. | 5m | Mittel | 4 |
| CryptoFrogHO3A4 | CryptoFrog-HO3-Variante. | 5m | Mittel | 4 |
| CryptoFrogNFI | CryptoFrog-Entry + NFI-artiger BB-Upper-Multi-Candle-Exit. | 5m | Mittel | 5 |
| CryptoFrogNFIHO1A | Hyperopt-Variante von CryptoFrogNFI. | 5m | Mittel | 4 |
| CryptoFrogOffset | CryptoFrog + MA-Offset-Logik & MACD. | 5m | Mittel | 5 |
| CustomStoplossWithPSAR | PSAR fallend als Entry + custom PSAR-Trailing-Stop. Eher Demo für custom_stoploss. | 1h | Mittel | 3 |
| DCBBBounce | Donchian+BB-Bounce mit SAR/SMA/EMA-50-Trendfilter. Trailing. | 5m | Mittel | 4 |
| DD | close<unteres BB & RSI<40; Exit oberes BB. Simple Mean-Reversion, tiefer Stop. | 5m | Mittel | 3 |
| DIV_v1 | RSI-Bullish-Divergenz + RSI<30. Divergenz-basiert, Trailing. | 5m | Mittel | 4 |
| DevilStra | „Spells": Multi-Indikator-Voting (Aroon/CCI/MACD/OBV/Stoch/WillR/T3). Elaboriert, 4h. | 4h | Mittel | 4 |
| Diamond | Generisches hyperoptbares Fast/Slow-Cross-Skelett (konfigurierbare Keys + Push-Offsets). Reine Optimierungs-Basis. | 5m | Mittel | 3 |
| Divergences | RSI≤40 + Bullish-Divergenz; Exit Bearish-Divergenz. Trailing. | 1h | Mittel | 4 |
| Dracula | Support-Level-Bounce + CMF>0 + Kerzenmuster + EMA-Schutz. | 5m | Mittel | 3 |
| Dyna_opti | 3-Tage-Tief + ADR-Positionierung (informative TF) + Cluc-BB-Spike. Range/Dip. | 5m | Mittel | 4 |
| EI3v2_tag_cofi_green | NFI-Lambo + EWO + Cofi (Stoch) + HMA-Exit, Tag-basiert. Multi-Signal. Kein Stop, Trailing. | 5m | Hoch | 5 |
| EMA50 | close kreuzt über EMA-50 (Exit unter). Simpler Breakout (großer ungenutzter Indikator-Import). Trailing. | 5m | Mittel | 3 |
| EMA520015_V17 | close kreuzt EMA-20 + custom Profit-Protect-Exit (ema20<ema200). Trailing. | 4h | Mittel | 3 |
| EMABBRSI | Multi-Entry: RSI>33 & Cross über BB-Lower3, EMA-200-Reclaim, EMA-50/200-Golden-Cross. | 1h | Mittel | 3 |
| EMABreakout | MACD-Hist≥0 + close kreuzt über EMA. Trailing-Breakout. | 5m | Mittel | 3 |
| EMASkipPump | close<EMA-short/medium & am Rolling-Min & ≤BB-Lower, Anti-Pump-Volume. Stop -5%. | 5m | Mittel | 3 |
| EMAVolume | EMA-13/34-Kreuzung + Volumen über Schnitt. Simpel. | 15m | Mittel | 3 |
| EMA_CROSSOVER_STRATEGY | EMA-10/100-Kreuzung. Klassischer MA-Cross (nutzt fragliche `.crossed_above`-Methode auf Series). | 5m | Mittel | 2 |
| EXPERIMENTAL_STRATEGY | RSI<35 & Stoch-fastd<35 & ADX>30 + DI (oder ADX>65); Exit RSI/fastd kreuzt 70. Oversold+Trend. | 5m | Mittel | 3 |
| ElliotV2 | ElliotV/SMAOffset-Lineage: close<MA·low_offset + EWO + RSI<Schwelle; Exit close>MA·high_offset. Bekannter Bull-Scalper. Stop -18%. | 5m | Mittel | 5 |
| ElliotV4 | ElliotV-Variante ohne echten Stop (-97%). Gleiche SMAOffset+EWO-Logik. | 5m | Hoch | 4 |
| ElliotV531 | ElliotV5 mit Multi-Hyperopt-ROI-Staffeln, Stop -18,9%. | 5m | Mittel | 5 |
| ElliotV5HO | Hyperopt-Variante der ElliotV5. | 5m | Mittel | 5 |
| ElliotV5HOMod2 | ElliotV5-HO ohne Stop (-99%), schlankere ROI. | 5m | Hoch | 4 |
| ElliotV5HOMod3 | ElliotV5-HO mit echtem Stop -6% (besseres Risikoprofil). | 5m | Mittel | 5 |
| ElliotV7 | ElliotV + uptrend_1h-Filter + rsi_fast + HMA-50-Exit. Ausgereiftere Iteration. | 5m | Mittel | 5 |
| ElliotV8HO | ElliotV8 hyperoptet, rsi_fast-Guard + HMA-Exit. | 5m | Mittel | 5 |
| ElliotV8_original | ElliotV8-Mainline (SMAOffset+EWO+rsi_fast, HMA-Exit). Stop -32%. | 5m | Mittel | 5 |
| ElliotV8_original_ichiv2 | ElliotV8 + Ichimoku-Informative-Filter. Stop -20%. | 5m | Mittel | 5 |
| ElliotV8_original_ichiv3 | Wie ichiv2, erweiterte ROI/Force-Exit-Staffel. | 5m | Mittel | 5 |
| Elliotv8 | ElliotV8-Mainline-Duplikat, Trailing aus. | 5m | Mittel | 5 |
| FRAYSTRAT | RSI-Cross + TEMA/BB-Guards + EMA-7/12-Kontext. Trailing. | 15m | Mittel | 3 |
| Fakebuy | Peak-Profit-Trailing + RMI + Cluc-BB-Spike. Eigenwillige Custom-Exit-Logik. | 5m | Mittel | 3 |
| FastSupertrend | Dreifach-Supertrend-Übereinstimmung (alle „up") Long, alle „down" Exit. Trailing. | 1h | Mittel | 4 |
| FastSupertrendOpt | FastSupertrend mit inline berechneten, hyperoptbaren Supertrends. | 1h | Mittel | 4 |
| FiveMinCrossAbove | RSI-8 kreuzt >30 & <41; kein echter Exit (close>1e10 → nur ROI). Kein Stop. | 5m | Hoch | 2 |
| FixedRiskRewardLoss | Keine Entry-Logik — Utility-Klasse für fixes Risk/Reward-custom_stoploss. | 5m | Niedrig | 2 |
| ForexSignal | EMA-Ribbon (8>13>21, 1h ausgerichtet) + Low<EMA-8-Pullback; Exit EMA-8 fallend. Stop -3%. | 5m | Mittel | 3 |
| FrostAuraM115mStrategy | FrostAura-Auto-Serie: close<BB-Lower2 (+Min-Preis); Exit RSI+BB. Hyperoptet je TF. | 15m | Hoch | 3 |
| FrostAuraM11hStrategy | FrostAura M1 auf 1h, Exit RSI>97 (absurd) → ROI-getrieben. Überangepasst. | 1h | Hoch | 2 |
| FrostAuraM21hStrategy | FrostAura M2: RSI+Stoch-Schwellen (hyperoptet). Tiefer Stop (-45%). | 15m | Hoch | 3 |
| FrostAuraM315mStrategy | FrostAura M3: RSI+Stoch+BB-Lower3. | 15m | Hoch | 3 |
| FrostAuraM31hStrategy | FrostAura M3 auf 1h. | 1h | Hoch | 3 |
| FrostAuraRandomStrategy | Entry/Exit per Zufallszahl + Wahrscheinlichkeit. Reine Benchmark/Null-Hypothese. | 1h | Hoch | 1 |
| GodCard | RSI>Schwelle & close unter BB-Lower/2/3 (tiefer Dip); Exit RSI+SAR+BB-Stack. Trailing. | 5m | Mittel | 3 |
| GodStraNew | „GodStra": genetisch evolvierte Strategie (Gen-DNA aus TA-Indikatoren, Logik nicht lesbar). Notorisch overfit. Kein Stop. | 4h | Hoch | 2 |
| GodStraNew40 | GodStra-Variante (40er-Gen-Satz). Gleiche GP-Overfit-Problematik. | 4h | Hoch | 2 |
| GodStraNew_SMAonly | GodStra auf SMA-Gene beschränkt, Trailing. | 5m | Hoch | 2 |
| Guacamole | KAMA-Cross + MACD + RMI + Volume-Cap; Exit RMI<30 & Profit-Guard. Trailing, kein Stop. | 5m | Hoch | 4 |
| Gumbo1 | EWO + T3/BB Multi-TF-Kombi; Exit Stoch/T3. | 5m | Mittel | 3 |
| Hacklemore2 | Up-Trend-Flag + RMI>55 + steigende Closes + SAR. Momentum-Continuation. Trailing, kein Stop. | 15m | Hoch | 3 |
| Hacklemore3 | Wie Hacklemore2 auf 5m, mit Profit-abhängigem Exit. | 5m | Hoch | 3 |
| HansenSmaOffsetV1 | high<SMA-Down-Offset & Heikin bullish. SMA-Offset-Mean-Reversion, kein Stop (-99). | 15m | Hoch | 3 |
| HarmonicDivergence | Harmonische Muster + Multi-Divergenz-Erkennung + Pivots. Genuin komplex. Trailing. | 15m | Mittel | 4 |
| Heracles | Generisches Indikator-vs-Cross-Skelett (Gen-Hyperopt). Trailing. | 12h | Mittel | 3 |
| HourBasedStrategy | Kauft/verkauft rein nach Tageszeit-Fenstern (Stunden-Saisonalität). Schwacher Edge. | 1h | Mittel | 2 |
| HyperStra_GSN_SMAOnly | GodStra-abgeleitetes SMA-only-Hyperopt-Skelett (Entry-Logik im Gen-Decode). | 5m | Mittel | 2 |
| HyperStra_SMAOnly | Wie oben, SMA-only-Hyperopt-Skelett. | 5m | Mittel | 2 |
| INSIDEUP | Kerzenmuster CDL3INSIDE (bullish) + RSI/ADX. Muster-basiert, kein Stop. | 1d | Hoch | 2 |
| Ichess | Ichimoku-„Score" (aggregiert) mit SMA-Fast/Slow-Kreuzung. Tageschart. | 1d | Mittel | 3 |
| Ichi | Preis bricht über Senkou-B (Cloud-Breakout, 1-Bar-Bestätigung). | 15m | Mittel | 3 |
| Ichimoku | Klassischer Tenkan/Kijun-Cross (TK-Cross) + Cloud-Farbe. Trailing. | 5m | Mittel | 3 |
| Ichimoku_SenkouSpanCross | Kumo-Twist (Senkou-A/B-Cross) + Preis über Cloud. Trailing, kein Stop. | 4h | Hoch | 3 |
| Ichimoku_v12 | Preis über Senkou-A & -B (über der Cloud). Simple Cloud-Trendfolge, kein Stop. | 4h | Hoch | 3 |
| Ichimoku_v30 | Cloud-Breakout (close kreuzt Senkou-A/B) + Doji-Star-Exit. Kein Stop. | 4h | Hoch | 3 |
| Ichimoku_v31 | HA-4h-Close kreuzt Senkou-A/B (Multi-TF); Exit Preis unter Cloud. Kein Stop. | 1h | Hoch | 3 |
| Ichimoku_v32 | Wie v30 auf Heikin-Ashi + TK-Cross-Exit. Kein Stop. | 4h | Hoch | 3 |
| Ichimoku_v33 | v30-Variante + SAR-Exit-Bestätigung. Kein Stop. | 4h | Hoch | 3 |
| Ichimoku_v37 | HA-4h-Close kreuzt 1d-Cloud (höheres TF-Kontext). Kein Stop. | 4h | Hoch | 3 |
| InformativeSample | EMA-20/50 + 15m-Informative-SMA-Filter. Freqtrade-Doku-Beispiel für Multi-TF. | 5m | Mittel | 3 |
| Inverse | Fisher-CCI-Cross + SSL-Channel + EMA-Trend (Multi-TF). Oszillator im Trendkontext. Trailing. | 1h | Mittel | 4 |
| InverseV2 | Iteration von Inverse, gleiche Fisher-CCI+SSL+EMA-Logik. | 1h | Mittel | 4 |
| JustROCR | Pur: Rate-of-Change-Ratio > 1,10 (Momentum-Breakout). Kein Exit-Signal. Trailing. | 1h | Mittel | 3 |
| JustROCR3 | Wie JustROCR, sehr enger Stop (-1%), höheres ROI-Ziel. | 5m | Mittel | 2 |
| JustROCR5 | Dual-ROCR-Momentum auf 1m. Sehr enger Stop. | 1m | Mittel | 2 |
| JustROCR6 | Multi-ROCR-Kaskade (5..499) als Momentum-Bestätigung. Trailing. | 1m | Mittel | 3 |
| KAMACCIRSI | KAMA/CCI/RSI, hyperoptet (Entry-Schwellen in Params → kauft breit). Trailing. | 5m | Mittel | 3 |
| KC_BB | Keltner-in-BB-Squeeze + Williams %R + Heikin-Ashi. Squeeze-Setup. Kein Stop. | 5m | Hoch | 3 |
| Kamaflage | KAMA-Cross + MACD + RMI + Volume-Cap (Guacamole-Verwandt). Trailing, kein Stop. | 5m | Hoch | 3 |
| Leveraged | EMA/BB-Dip am Rolling-Min + steigender Durchschnitt; Exit an Hochs + MFI. Stop -5%. | 5m | Mittel | 3 |
| LookaheadStrategy | EMA-Cross mit shift-Parametern; Name deutet auf Lookahead-Demo hin — mit Vorsicht (mögliche Bias). | 5m | Hoch | 2 |
| Low_BB | close≤0,98·unteres BB. Kein Exit-Signal, sehr enger Stop (-1,5%). | 1m | Mittel | 2 |
| LuxOSC | LuxAlgo-artiger Oszillator-Cross + Supertrend-Filter. Kein Stop. | 5m | Hoch | 3 |
| MAC | EMA-50/200 Golden/Death-Cross auf Tageschart. Klassiker. | 1d | Mittel | 3 |
| MACDCCI | MACD>Signal & CCI≤-100. Momentum+Oversold. | 30m | Mittel | 3 |
| MACDRSI200 | Rolling-RSI<41 & close>EMA-200 & MACD-Cross. Trend-Pullback, enger Stop (-4%). | 5m | Mittel | 3 |
| MACDStrategy | MACD-Cross + CCI-Filter (hyperoptbar). | 5m | Mittel | 3 |
| MACDStrategy_crossed | Wie MACDStrategy mit fixen CCI-Schwellen (-50/100). | 5m | Mittel | 3 |
| MACD_EMA | MACD-Cross + close>EMA-Long-Trendfilter. | 5m | Mittel | 3 |
| MACD_TRIPLE_MA | MACD-Cross + SMA-6/14-Cross + SMA-26-Filter. Trailing, enger Stop (-3%). | 5m | Mittel | 3 |
| MACD_TRI_EMA | MACD-Cross + TEMA-Bestätigung. Enger Stop (-3%). | 5m | Mittel | 3 |
| MADisplaceV3 | NFI-artig: rsi_slow fallend + rsi_fast + Uptrend + MA-Lower-Dip (MA-Displacement). Trailing. | 5m | Mittel | 4 |
| MFI | Pur: MFI≤14 Entry, ≥75 Exit. Money-Flow-Oversold. | 5m | Mittel | 3 |
| Macd | Tages-MACD-Histogramm>0 als Regime (1d informative). Simpel. | 1h | Mittel | 3 |
| MacheteV8b | Multi-TF-Komplex: SSL + Ichimoku-Informative + MACD + AO + ADX. Elaboriert. | 15m | Mittel | 4 |
| MacheteV8bRallimod2 | Machete + ElliotV-SMAOffset-Entry, Ichimoku-Informative-Exit. | 5m | Mittel | 4 |
| MarketChyperHyperStrategy | Regime-adaptiv (down/side/up) WaveTrend-Oversold + Signal-Strength-Voting. Trailing. | 1h | Mittel | 4 |
| Maro4hMacdSd | MACD-Histogramm-Reversal-Muster + Korrelations-Filter. | 5m | Mittel | 3 |
| Martin | RSI-Cross 30 + TEMA/BB-Guards (Freqtrade-Sample-artig). | 5m | Mittel | 2 |
| MiniLambo | NFI-Lambo: close<EMA-14·Faktor + RSI-4/14 + pct_change-Fenster. | 1m | Mittel | 4 |
| Minmax | Nutzt Extrema-Erkennung (argrelextrema) für Sell-Signal. Lookahead-anfällig. | 1h | Mittel | 2 |
| MomStrategy | Vorberechnetes Momentum-„signal"==1/-1. Kein Stop. | 1h | Hoch | 3 |
| Momentumv2 | MACD-Cross + close>EMA; Exit MACD-/RSI-Cross. | 4h | Mittel | 3 |
| MontrealStrategy | RSI>30 & close<BB2-Lower; Exit close>BB2-Upper. BB-Mean-Reversion. | 15m | Mittel | 3 |
| MostOfAll | MOST-Indikator (MA+Trailing) Cross + Alligator/Fractal-Kontext. | 5m | Mittel | 3 |
| MultiMA_TSL | MA-Offset-Confluence (EMA/ZEMA/TRIMA) + EWO + RSI, custom TSL. SMAOffset-Lineage. | 5m | Mittel | 4 |
| MultiMA_TSL3 | MultiMA-Erweiterung + PMAX-Threshold. | 5m | Mittel | 4 |
| MultiMA_TSL3_Mod | MultiMA_TSL3 + SAR/PMAX-Modifikation. | 5m | Mittel | 4 |
| MultiMa | Confluence mehrerer MAs auf 4h, tiefer Stop (-34,5%). | 4h | Hoch | 3 |
| MultiOffsetLamboV0 | Multi-MA-Offset + Lambo-Dip-Entry. Stop -50%. | 5m | Hoch | 4 |
| MultiRSI | Mehrere RSI-Perioden als Oversold-Confluence. Stop -5%. | 5m | Mittel | 3 |
| NASOSRv6_private_Reinuvader_20211121 | NASOS (Not Another Stupid Osc.) — ElliotV-abgeleiteter SMAOffset+EWO-Scalper; Community-Snapshot (Reinuvader). Bull-Scalper mit custom Exit. | 5m | Mittel | 5 |
| NASOSv4 | NASOS v4: close<MA·Offset + EWO + RSI + rsi_fast, HMA-Exit. Sehr populär. Stop -15%. | 5m | Mittel | 5 |
| NASOSv5 | NASOS v5, verfeinerte SMAOffset+EWO-Logik + custom Sell/Trailing. | 5m | Mittel | 5 |
| NASOSv5_mod1 | NASOSv5-Mod, Trailing, Stop -30%. | 5m | Hoch | 5 |
| NASOSv5_mod1_DanMod | NASOSv5_mod1 Community-Tuning (DanMod). | 5m | Hoch | 5 |
| NASOSv5_mod2 | NASOSv5-Mod-Variante. | 5m | Hoch | 5 |
| NASOSv5_mod3 | NASOSv5-Mod-Variante. | 5m | Hoch | 5 |
| NFI46 | NostalgiaForInfinity v4.6: Dutzende Buy-Conditions + Protections + Multi-TF. Anspruchsvollste öffentliche Lineage. Custom-Stop (Hard -99%). | 5m | Hoch | 6 |
| NFI46Frog | NFI 4.6 × CryptoFrog-Merge. | 5m | Hoch | 5 |
| NFI46FrogZ | NFI46Frog-Variante (Z-Tuning). | 5m | Hoch | 5 |
| NFI46Offset | NFI 4.6 + MA-Offset-Entry. | 5m | Hoch | 5 |
| NFI46OffsetHOA1 | NFI46Offset hyperoptet. | 5m | Hoch | 5 |
| NFI46Z | NFI 4.6 Z-Variante. | 5m | Hoch | 5 |
| NFI47V2 | NostalgiaForInfinity v4.7 (V2). | 5m | Hoch | 6 |
| NFI4Frog | NFI v4 × CryptoFrog-Merge. | 5m | Hoch | 5 |
| NFI5MOHO | NFI v5 „MultiOffset+HyperOpt", echter Stop -10%, Trailing. | 5m | Mittel | 5 |
| NFI5MOHO2 | NFI5MOHO-Variante, kein Hard-Stop. | 5m | Hoch | 5 |
| NFI5MOHO_WIP | NFI5MOHO Work-in-Progress. | 5m | Hoch | 5 |
| NFI5MOHO_WIP_1 | NFI5MOHO-WIP-Iteration, Trailing. | 5m | Hoch | 5 |
| NFI5MOHO_WIP_2 | NFI5MOHO-WIP-Iteration. | 5m | Hoch | 5 |
| NFI731_BUSD | NFI v7.3.1 (BUSD-Paare). | 5m | Hoch | 6 |
| NFI7MOHO | NFI v7 MultiOffset+HyperOpt. | 5m | Hoch | 5 |
| NFINextMOHO | NFI-Next MultiOffset+HyperOpt. | 5m | Hoch | 5 |
| NFINextMOHO2 | NFINextMOHO-Variante. | 5m | Hoch | 5 |
| NFINextMultiOffsetAndHO | NFI-Next + MultiOffset-Confluence + HyperOpt. | 5m | Hoch | 5 |
| NFINextMultiOffsetAndHO2 | Variante mit Trailing. | 5m | Hoch | 5 |
| NFIX_BB_RPB | NFI-X × BB_RPB_TSL-Merge. | 5m | Hoch | 5 |
| NFIX_BB_RPB_c7c477d_20211030 | Datierter Snapshot des NFIX×RPB-Merges. | 5m | Hoch | 5 |
| NfiNextModded | NFI-Next Community-Mod, Stop -50%. | 5m | Hoch | 5 |
| NormalizerStrategy | Normalisiert Indikatoren (0–1) für vergleichbare Schwellen. Trailing, kein Hard-Stop. | 1h | Hoch | 3 |
| NormalizerStrategyHO2 | Hyperopt-Variante der NormalizerStrategy. | 1h | Hoch | 3 |
| Nostalgia | Frühe/abgespeckte NFI-Version. | 5m | Hoch | 5 |
| NostalgiaForInfinityNext | NFI-Next-Mainline: die meistgepflegte öffentliche Strategie überhaupt (viele Conditions, Protections, Grinding, custom Stop). | 5m | Hoch | 6 |
| NostalgiaForInfinityNextGen | NFI-NextGen auf 15m, Stop -50%. | 15m | Hoch | 6 |
| NostalgiaForInfinityNextGen_TSL | NextGen + Trailing/echter Stop -10%. Besseres Risikoprofil. | 15m | Mittel | 6 |
| NostalgiaForInfinityNextV7155 | NFI-Next v7.15.5, Stop -50%. | 5m | Hoch | 6 |
| NostalgiaForInfinityNext_ChangeToTower_V5_2 | NFI-Next Community-Fork (ChangeToTower V5.2). | 5m | Hoch | 5 |
| NostalgiaForInfinityNext_ChangeToTower_V5_3 | ChangeToTower V5.3. | 5m | Hoch | 5 |
| NostalgiaForInfinityNext_ChangeToTower_V6 | ChangeToTower V6. | 5m | Hoch | 5 |
| NostalgiaForInfinityNext_maximizer | NFI-Next mit maximizer-Tuning. | 5m | Hoch | 5 |
| NostalgiaForInfinityV1 | NFI v1 (frühe Mainline), Trailing, Stop -36%. | 5m | Hoch | 5 |
| NostalgiaForInfinityV2 | NFI v2 Mainline. | 5m | Hoch | 6 |
| NostalgiaForInfinityV3 | NFI v3 Mainline. | 5m | Hoch | 6 |
| NostalgiaForInfinityV4 | NFI v4 Mainline. | 5m | Hoch | 6 |
| NostalgiaForInfinityV4HO | NFI v4 hyperoptet. | 5m | Hoch | 5 |
| NostalgiaForInfinityV5 | NFI v5 Mainline. | 5m | Hoch | 6 |
| NostalgiaForInfinityV5MultiOffsetAndHO | NFI v5 + MultiOffset-Confluence + HyperOpt. | 5m | Hoch | 5 |
| NostalgiaForInfinityV5MultiOffsetAndHO2 | Variante davon. | 5m | Hoch | 5 |
| NostalgiaForInfinityV6 | NFI v6 Mainline. | 5m | Hoch | 6 |
| NostalgiaForInfinityV6HO | NFI v6 hyperoptet. | 5m | Hoch | 5 |
| NostalgiaForInfinityV7 | NFI v7 Mainline — reifer, stark gepflegter Meilenstein. | 5m | Hoch | 6 |
| NostalgiaForInfinityV7_7_2 | NFI v7.7.2 Punkt-Release. | 5m | Hoch | 6 |
| NostalgiaForInfinityV7_SMA | NFI v7 + SMAOffset, Trailing. | 5m | Hoch | 6 |
| NostalgiaForInfinityV7_SMAv2 | NFI v7 SMAOffset v2. | 5m | Hoch | 6 |
| NostalgiaForInfinityV7_SMAv2_1 | NFI v7 SMAOffset v2.1. | 5m | Hoch | 6 |
| NostalgiaForInfinityX | NFI-X (Experimental-Zweig der Lineage). | 5m | Hoch | 6 |
| NostalgiaForInfinityX2 | NFI-X2. | 5m | Hoch | 6 |
| NostalgiaForInfinityXw | NFI-X Community-Variante (w). | 5m | Hoch | 5 |
| NotAnotherSMAOffSetStrategy_V2 | Kanonische NASOS/SMAOffset: close<MA·Offset + EWO + RSI; HMA-basierter Exit. Trailing, Stop -35%. | 5m | Hoch | 5 |
| NotAnotherSMAOffsetStrategy | NASOS-Original (SMAOffset+EWO-Scalper). | 5m | Hoch | 5 |
| NotAnotherSMAOffsetStrategyHO | NASOS hyperoptet. | 5m | Hoch | 5 |
| NotAnotherSMAOffsetStrategyHOv3 | NASOS-HO v3, Stop -30%. | 5m | Hoch | 5 |
| NotAnotherSMAOffsetStrategyLite | Abgespeckte NASOS, echter Stop -10%. | 5m | Mittel | 5 |
| NotAnotherSMAOffsetStrategyModHO | NASOS-Mod hyperoptet, Stop -32%. | 5m | Hoch | 5 |
| NotAnotherSMAOffsetStrategyModHO_LamineDz_20210901 | Community-Snapshot (LamineDz), Stop -90%. | 5m | Hoch | 5 |
| NotAnotherSMAOffsetStrategyX1 | NASOS-X1-Variante. | 5m | Hoch | 5 |
| NotAnotherSMAOffsetStrategy_uzi | NASOS Community-Tuning (uzi), echter Stop -7%. | 5m | Mittel | 5 |
| NotAnotherSMAOffsetStrategy_uzi3 | NASOS uzi v3, Stop -10%. | 5m | Mittel | 5 |
| NowoIchimoku1hV1 | Ichimoku mit verschobener-Cloud-Confluence + Conversion/Base-Line. Trend-Breakout. Stop -8%. | 1h | Mittel | 4 |
| NowoIchimoku1hV2 | Wie V1, hyperoptbare Cloud-Faktoren, Trailing. | 1h | Mittel | 4 |
| NowoIchimoku5mV2 | 5m-Port mit Zeitfaktor-Skalierung der Ichimoku-Shifts. | 5m | Mittel | 3 |
| ONUR | RSI<74 & close>BB-Mitte (RSI<74 fast immer wahr → trivial). Kein Stop. | 15m | Hoch | 2 |
| ObeliskIM_v1_1 | Obelisk-Ichimoku: starke grüne Cloud + TK-Cross-Up + EMA-35 + Breakout + Spike-Filter. Enger Stop (-4%). | 5m | Mittel | 4 |
| ObeliskRSI_v6_1 | Regime-bewusstes RSI (Bull/Bear unterschiedliche Schwellen). | 5m | Mittel | 3 |
| Obelisk_3EMA_StochRSI_ATR | 3-EMA-Trend + Stoch-RSI + ATR (go_long-Regime). Kein Stop. | 5m | Hoch | 3 |
| Obelisk_Ichimoku_Slow_v1_3 | Langsame Ichimoku-Trendfolge. Trailing, kein Hard-Stop. | 1h | Hoch | 4 |
| Obelisk_Ichimoku_ZEMA_v1 | Ichimoku + ZEMA-Glättung. | 5m | Mittel | 3 |
| Obelisk_TradePro_Ichi_v1_1 | TradePro-YouTube-Ichimoku (TK-Cross + Cloud + Chikou). Sehr enger Stop (-1,5%). | 1h | Mittel | 3 |
| Obelisk_TradePro_Ichi_v2_1 | TradePro-Ichimoku v2, Trailing, Stop -7,5%. | 1h | Mittel | 4 |
| PRICEFOLLOWING | RSI + EMA-7/TEMA-Cross (Fisher/HA/MACD/SAR-Ensemble). Trailing. | 5m | Mittel | 3 |
| PRICEFOLLOWING2 | Price-Following-Variante auf 15m. | 15m | Mittel | 3 |
| PRICEFOLLOWINGX | Price-Following X, Stop -50%. | 15m | Hoch | 3 |
| Persia | Generisches hyperoptbares {Indikator}-{TF}-Cross-Skelett (EMA/RSI/SMA/TEMA). Stop -19%. | 5m | Mittel | 3 |
| PrawnstarOBV | OBV kreuzt OBV-SMA + RSI<50. Volumen-basiert. Trailing. | 1h | Mittel | 3 |
| PumpDetector | KDJ-„J" kreuzt 0 (Pump-Erkennung); Exit bei J>90. Kein Stop. | 5m | Hoch | 3 |
| Quickie | ADX>30 + TEMA steigt unter BB-Mitte + SMA-200>close (Dip im Abwärtstrend). Stop -25%. | 5m | Mittel | 3 |
| RSI | Pur RSI + Williams-%R-Multi-TF-Exit. Kein Stop. | 15m | Hoch | 3 |
| RSIBB02 | RSI>19 & close<unteres BB. BB/RSI-Mean-Reversion. | 1h | Mittel | 3 |
| RSIv2 | Williams-%R<-80 & RSI<30 (Oversold-Confluence). Kein Stop. | 15m | Hoch | 3 |
| RalliV1 | SMAOffset (MA-buy<EMA-100 + SMA-9<MA-buy). NASOS-verwandt. Stop -30%. | 5m | Hoch | 4 |
| RalliV1_disable56 | RalliV1 mit deaktivierten Conditions 5/6. | 5m | Hoch | 4 |
| RaposaDivergenceV1 | Preis/RSI-Divergenz an lokalen Tiefs. Trailing. | 5m | Hoch | 4 |
| ReinforcedAverageStrategy | MA-Kreuzung + resampelter SMA-Trendfilter. | 4h | Mittel | 3 |
| ReinforcedQuickie | EMA-Dip-Scalp + Trend, enger Stop (-5%). | 5m | Mittel | 3 |
| ReinforcedSmoothScalp | open<EMA-Low + ADX>30 + Stoch (SmoothScalp). | 1m | Mittel | 3 |
| Renko | Renko-Brick-Logik auf 15m-Kerzen. Kein Stop (-100). | 15m | Hoch | 3 |
| RobotradingBody | Kerzenkörper > Körper-SMA (große Kerze). Kein Stop. | 4h | Hoch | 3 |
| Roth01 | MFI<24 & close<unteres BB. Oversold-Mean-Reversion. | 5m | Mittel | 3 |
| Roth03 | close<unteres BB & Stoch-fastd>37. | 5m | Mittel | 3 |
| SAR | RSI kreuzt 30 + TEMA/BB-Guards (Sample-artig, trotz Name kein SAR-Kern). | 5m | Mittel | 2 |
| SMAIP3 | SMAOffset + „pair_is_bad"-Filter (pumpende Paare aussieben). Trailing. | 5m | Hoch | 4 |
| SMAIP3v2 | SMAIP3-Iteration, Stop -23%. | 5m | Hoch | 4 |
| SMAOG | SMAOffset „OG"-Variante mit Bad-Pair-Filter. Trailing. | 5m | Hoch | 4 |
| SMAOPv1_TTF | SMAOffset + EWO (TTF-Tuning). Stop -50%. | 5m | Hoch | 4 |
| SMAOffset | Kanonische SMAOffset-Basis: close<MA·Offset. Ursprung der NASOS/ElliotV-Lineage. Stop -50%. | 5m | Hoch | 4 |
| SMAOffsetProtectOpt | SMAOffset + EWO + Protections, hyperoptet. Stammbaum der SMAOffset-Familie. | 5m | Hoch | 5 |
| SMAOffsetProtectOptV0 | SMAOffsetProtect V0. | 5m | Hoch | 5 |
| SMAOffsetProtectOptV1 | SMAOffsetProtect V1 (verbreitetste Version). | 5m | Hoch | 5 |
| SMAOffsetProtectOptV1HO1 | V1 hyperoptet. | 5m | Hoch | 5 |
| SMAOffsetProtectOptV1Mod | V1-Community-Mod. | 5m | Hoch | 5 |
| SMAOffsetProtectOptV1Mod2 | V1-Mod-Iteration. | 5m | Hoch | 5 |
| SMAOffsetProtectOptV1_kkeue_20210619 | V1-Snapshot (kkeue). | 5m | Hoch | 5 |
| SMAOffsetV2 | SMAOffset + go_long-Regime-Gate. Stop -20%. | 5m | Hoch | 4 |
| SMA_BBRSI | Anti-Pump-Filter + SMAOffset-Entry. | 5m | Hoch | 4 |
| SRsi | Stoch-RSI: K<15 & K≥D (Oversold-Turn). | 1m | Mittel | 3 |
| STRATEGY_RSI_BB_BOUNDS_CROSS | Vergleich RSI-normiert vs. BB-normiert (Bounds-Trend). Ungewöhnlicher Ansatz. | 5m | Mittel | 3 |
| STRATEGY_RSI_BB_CROSS | BB-Percent kreuzt RSI-Percent & BB<0,5. | 5m | Mittel | 3 |
| SampleStrategy | Trotz Name NFI-artige Protection-Struktur (EMA-Stacks + Multi-TF). | 5m | Hoch | 4 |
| SampleStrategyV2 | RSI-Cross + HA-SMA-288-Trendrichtung. Trailing. | 5m | Mittel | 3 |
| Saturn5 | VW-MACD + EMA-Stack + Fib/BB-Bänder (Apollo11-artig). | 15m | Mittel | 4 |
| Scalp | Klassischer Freqtrade-Scalp: open<EMA-Low + ADX>30 + Stoch. Enger Stop (-4%). | 1m | Mittel | 3 |
| Schism | RMI-Uptrend + dynamischer Peak-Profit-Exit (informative TF, Custom-Bailout). Durchdachte Exit-Logik. | 5m | Hoch | 4 |
| Schism2 | Schism-Iteration, Stop -30%. | 5m | Hoch | 4 |
| Schism2MM | Schism2 Money-Management-Variante, kein Hard-Stop. | 5m | Hoch | 4 |
| Schism3 | Schism + „bounce-pending"-Logik & Multi-TF-RSI. | 5m | Hoch | 4 |
| Schism4 | Schism-Iteration. | 5m | Hoch | 4 |
| Schism5 | Schism-Iteration. | 5m | Hoch | 4 |
| Schism6 | Schism-Iteration, Stop -50%. | 5m | Hoch | 4 |
| Seb | EMA-20/50-Cross + Heikin-Ashi-Bestätigung. | 5m | Mittel | 3 |
| Simple | MACD>0 & MACD>Signal. Simpler Momentum-Long. Stop -25%. | 5m | Mittel | 3 |
| SlowPotato | Low ≤ 1440-Perioden-Durchschnitts-Low (unter Tagesschnitt). Simple Mean-Reversion, kein Stop. | 5m | Hoch | 3 |
| Slowbro | close kreuzt über 30-Tage-Tief (informative). Range-Ausbruch, kein Stop. | 1h | Hoch | 3 |
| SmoothOperator | Steigender Durchschnitt + Multi-Indikator-Bestätigung. Enger Stop (-5%). | 5m | Mittel | 3 |
| SmoothScalp | open<EMA-Low + Stoch-Scalp. Stop -50%. | 1m | Hoch | 3 |
| Stavix2 | close>Senkou-A (Ichimoku-Cloud-Long). | 1m | Mittel | 3 |
| Stinkfist | RMI-Uptrend + dynamischer Peak-Profit-Exit (Schism-Autor). Trailing. | 5m | Hoch | 4 |
| StochRSITEMA | Stoch-RSI + TEMA (hyperoptbar). Trailing, enger Stop (-2,2%). | 5m | Mittel | 3 |
| Strategy001 | „berlinguyinca"-Set: EMA-20/50-Cross + Guards. | 5m | Mittel | 3 |
| Strategy001_custom_sell | Strategy001 + Custom-Sell-Logik. | 5m | Mittel | 3 |
| Strategy002 | RSI<30 + Stoch/Fisher-Guards. | 5m | Mittel | 3 |
| Strategy003 | RSI<28 + Guards. | 5m | Mittel | 3 |
| Strategy004 | ADX>50-getrieben. | 5m | Mittel | 3 |
| Strategy005 | Multi-Indikator-Set-Variante. | 5m | Mittel | 3 |
| StrategyScalpingFast | 1m-Scalp (EMA-Low + Stoch). Stop -50%. | 1m | Hoch | 2 |
| StrategyScalpingFast2 | Scalp-Variante, hyperoptbare Conditions. | 1m | Mittel | 3 |
| SuperHV27 | „SuperHold V27" (BinHV27-Verwandt, RMI-Trend). Stop -40%. | 5m | Hoch | 4 |
| SuperTrend | Dreifach-Supertrend-Übereinstimmung. Trailing. | 1h | Mittel | 4 |
| SuperTrendPure | close kreuzt über Supertrend (pur). Trailing. | 1h | Mittel | 4 |
| SupertrendStrategy | Summe der Supertrend-Richtungen als Trend-Score. Kein Stop. | 1h | Hoch | 3 |
| SwingHigh | MACD-basiertes Swing-Setup. Trailing. | 30m | Mittel | 3 |
| SwingHighToSky | CCI-basiertes Swing-Setup (hyperoptbare CCI-Zeit/Schwelle). | 15m | Mittel | 3 |
| TDSequentialStrategy | TD-Sequential (DeMark) Count>8. Enger Stop (-5%). | 1h | Mittel | 4 |
| TEMA | TEMA/BB-Sample-Logik. | 1m | Mittel | 2 |
| TechnicalExampleStrategy | CMF<0-Demo für die technical-Lib. Eher Lehrbeispiel. | 5m | Mittel | 2 |
| TemaMaster | TEMA kreuzt über unteres BB (Mean-Reversion). Trailing. | 5m | Mittel | 3 |
| TemaMaster3 | TemaMaster-Iteration auf 1m. | 1m | Mittel | 3 |
| TemaPure | TEMA≤unteres BB (pur). Trailing. | 5m | Mittel | 3 |
| TemaPureNeat | Aufgeräumte TemaPure-Variante. | 5m | Mittel | 3 |
| TemaPureTwo | TemaPure-Variante. | 5m | Mittel | 3 |
| TenderEnter | RMI/Trend-Entry. Trailing, Stop -40%. | 15m | Hoch | 3 |
| TheForce | „TheForce"-Scalp: Stoch-fastk 20–80 + EMA + MACD. Sehr enger Stop (-1,5%). | 15m | Mittel | 3 |
| TheRealPullbackV2 | Pullback-Entry im Trend. Enger Stop (-3,5%). | 5m | Mittel | 3 |
| TrailingBuyStrat2 | Trailing-Buy-Mixin/Basis (kein eigenständiges Signal/Timeframe). Framework-Baustein. | – | Mittel | 2 |
| Trend_Strength_Directional | DI+/DI- Richtung + ADX-Stärke. Trailing. | 15m | Mittel | 3 |
| TrixStrategy | TRIX-Histogramm>0 (Momentum-Trend). Kein Stop. | 1h | Hoch | 3 |
| TrixV15Strategy | „Trix"-Community-Strategie v15 (TRIX + EMA/Stoch-Guards). Stop -31%. | 1h | Mittel | 4 |
| TrixV21Strategy | Trix v21-Variante. | 1h | Mittel | 4 |
| TrixV23Strategy | Trix v23-Variante. | 1h | Mittel | 4 |
| UltimateMomentumIndicator | UTMI (kombinierter Momentum-Index) kreuzt 50. Kein Stop. | 5m | Hoch | 3 |
| Uptrend | RSI<80 + Trend-Guards (RSI<80 fast immer). | 5m | Mittel | 2 |
| UziChan | UziChannel-Breakout nach unten (Dip-Kauf am Kanalboden). | 5m | Mittel | 3 |
| UziChan2 | UziChan auf 1m. | 1m | Mittel | 3 |
| VWAP | close<VWAP-Unterband (VWAP-Mean-Reversion). | 5m | Mittel | 3 |
| WaveTrendStra | WaveTrend wt1/wt2-Kreuzung. | 4h | Mittel | 3 |
| XebTradeStrat | EMA-5/10 + Guards. Sehr enger Stop (-1%). | 1m | Mittel | 3 |
| XtraThicc | Kerzenfarbe grün + Guards. | 5m | Mittel | 3 |
| YOLO | ADX + hyperoptete Guards. Sehr enger Stop (-1%). | 1m | Mittel | 2 |
| adaptive | MAMA/FAMA adaptive MA (KAMA>FAMA). Trendfolge. | 5m | Mittel | 3 |
| adx_opt_strat | ADX + Momentum, hyperoptet. Trailing. | 1m | Mittel | 3 |
| adxbbrsi2 | ADX>47 + BB + RSI. Trend+Oversold. Trailing. | 1h | Mittel | 3 |
| bb_rsi_opt_new | RSI>28 + BB (hyperoptet). Trailing. | 1h | Mittel | 3 |
| bbema | BB+EMA — nutzt `close.shift(-10)` (negativer Shift) → **Lookahead-Bias**, unbrauchbar live. | 1h | Hoch | 1 |
| bbrsi1_strategy | RSI<30 & close<unteres BB. Klassik-Mean-Reversion. | 5m | Mittel | 3 |
| bbrsi4Freq | close<unteres BB3. Trailing. | 1h | Mittel | 3 |
| bestV2 | SMAOffset (close<MA·low_offset) — NASOS-verwandt. Trailing. | 5m | Mittel | 4 |
| botbaby | EMA-13>50 + Guards. Extrem enger Stop (-0,7%). | 30m | Mittel | 3 |
| conny | Technical-„consensus"-Score>45 (Indikator-Voting). Enger Stop (-2%). | 15m | Mittel | 3 |
| cryptohassle | Heikin-Ashi + SSL-Cross. Trailing. | 1h | Mittel | 3 |
| custom | Anti-Pump-Filter + Multi-Indikator-Entry. | 5m | Mittel | 3 |
| custom_sell | Keltner-basiert + Custom-Sell-Logik. Stop -34,7%. | 5m | Hoch | 3 |
| e6v34 | HMA-Steigungs-Differenzen (HMA-Slope). Trailing, Stop -54%. | 15m | Hoch | 3 |
| ema | EMA/EMA2-Kreuzung. Kein Stop (-100). | 5m | Hoch | 2 |
| epretrace | Generisches Entry-Point-Retracement-Skelett (hyperopt). Kein Stop (-99,9%). | 5m | Hoch | 3 |
| fahmibah | NFI-Lambo (ha_close<EMA-14·Faktor + RSI). | 5m | Mittel | 3 |
| flawless_lambo | Lambo-Dip-Buyer. Kein Stop (-100). | 15m | Hoch | 3 |
| hansencandlepatternV1 | Kerzenmuster (3-Line-Strike, Evening-Star, Abandoned-Baby). Muster-basiert. | 1h | Mittel | 2 |
| heikin | Heikin-Ashi EMA-Open/Close-Cross. Kein Stop. | 1h | Hoch | 3 |
| hlhb | „Little Handy Bot": RSI-Cross 50 + EMA + ADX (Forex-Trend-Stil). Trailing. | 4h | Mittel | 3 |
| ichiV1 | Bekannte Ichimoku-Strategie: trend_close vs. Senkou + Cloud + Chikou. Solide Trendfolge. Stop -27,5%. | 5m | Mittel | 5 |
| ichiV1_Marius | ichiV1 + BTC-Safe-Filter + Position-Adjustment (DCA). | 5m | Mittel | 5 |
| ichiV1_futures | Futures/Short-fähige ichiV1-Variante — **die im Repo validierte, live (Dry-Run auf WEEX) laufende Strategie**; OOS fee-aware getestet (~+42%, aber ROI-abhängig & short-lastig). can_short, echter Stop -5%. | 5m | Mittel | 5 |
| keltnerchannel | close kreuzt über Keltner-Oberband (Breakout). | 6h | Mittel | 3 |
| mabStra | MA + Divergenz-Filter. | 4h | Mittel | 3 |
| macd_recovery | Rolling-RSI<41 + MACD-Recovery. Enger Stop (-4%). | 5m | Mittel | 3 |
| mark_strat | close<unteres BB (Mean-Reversion). Trailing. | 1m | Mittel | 3 |
| mark_strat_opt | mark_strat + ADX>49-Filter (hyperoptet). | 1m | Mittel | 3 |
| quantumfirst | Multi-Indikator-Set (Mindestpreis-Filter + Guards). | 5m | Mittel | 3 |
| redditMA | MA-Strategie (Reddit-Ursprung). Stop -50%. | 15m | Hoch | 3 |
| stoploss | RSI kreuzt 30 (Sample-artig, trotz Name kein Stop-Fokus). | 5m | Mittel | 2 |
| stratfib | RSI-Cross + Fibonacci-Level. | 1h | Mittel | 3 |
| strato | Stochastic K<18 (Oversold). | 1m | Mittel | 3 |
| true_lambo | Pump-Erkennung (Rolling-Max-Faktor). Kein Stop. | 5m | Hoch | 3 |
| wtc | WaveTrend wt1/wt2-Kreuzung. | 30m | Mittel | 3 |
### Fazit & Einordnung

- **Kein Backtest ersetzt** — die Bewertungen sind typbasierte Einschätzungen. Vor jedem Live-Einsatz gilt: fee-aware Backtest + Out-of-Sample-Validierung + `lookahead-analysis`.
- **Höchste Ratings (6):** die **NostalgiaForInfinity (NFI)**-Mainline (V2–V7, X, Next, 731) — mit Abstand die am besten konstruierten und gepflegtesten öffentlichen Strategien (viele Entry-Conditions, Protections, custom Stop). Aber: schwergewichtig, komplex und **auch sie sind kein garantierter Edge**.
- **Solide (5):** die SMAOffset-Lineage (**NASOS/NotAnotherSMAOffset**, **ElliotV**, **SMAOffsetProtectOpt**), **CryptoFrog**, **BB_RPB_TSL_SMA_Tranz**, sowie **ichiV1 / ichiV1_futures** (letztere ist die im Repo validierte, live laufende Strategie).
- **Struktureller Vorbehalt:** Sehr viele Strategien (v.a. Cluc/BinH/BigZ/BinClucMad-Dip-Buyer) nutzen `stoploss = -0.99` (praktisch **kein Hard-Stop**) + winzige ROI. Sie sammeln viele Mini-Gewinne und verstecken das Risiko in seltenen, katastrophalen Drawdowns (Crash-Anfälligkeit). Hohes „Risiko" in der Tabelle = genau das.
- **1–2 = Finger weg:** Platzhalter/Tests (AlwaysBuy, BuyAll…, BreakEven, FrostAuraRandom), kaputte/triviale Logik oder Lookahead-Bias (bbema, LookaheadStrategy).
- Die vielen `*HO`/`*Opt`-Varianten sind hyperoptete Ableitungen — höheres Overfitting-Risiko als ihre Basis; im Zweifel die Mainline-Version bevorzugen und selbst neu optimieren.
