# MOVING AVERAGE
#
# Trading algorithm that uses long-term and medium/short-term moving averages
#


import pandas as pd


def moving_average(closing_prices: pd.Series, days):
    return closing_prices.rolling(days).mean().dropna()


def determine_signal(long_ma, short_ma, curr_run, padding=0):
    if long_ma > short_ma + padding:
        # bullish -> bearish; death cross, short
        if curr_run == "bullish":
            return "sell", "bearish"
        # bearish -> bearish
        elif curr_run == "bearish":
            return "none", "bearish"
        else:
            return "none", "bearish"
    elif long_ma + padding < short_ma:
        # bullish -> bullish
        if curr_run == "bullish":
            return "none", "bullish"
        # bearish -> bullish; golden cross, buy with stop loss
        elif curr_run == "bearish":
            return "buy", "bullish"
        # unknown -> bullish; golden cross, buy with stop loss
        else:
            return "buy", "bullish"
    else:
        return "none", "neutral"
