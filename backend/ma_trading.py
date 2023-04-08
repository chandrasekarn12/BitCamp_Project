import pandas as pd


def moving_average(closing_prices: pd.Series, days):
    return closing_prices.rolling(days).mean().dropna()

