# import necessary libraries
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from mplfinance.original_flavor import candlestick_ohlc
import math
import numpy as np
import yfinance as yf
import pandas as pd
# !pip install yfinance
# !pip install mplfinance
# get stock prices using yfinance library


def get_stock_price(symbol):
    df = yf.download(symbol, start='2021-02-01', threads=False)
    df['Date'] = pd.to_datetime(df.index)
    df['Date'] = df['Date'].apply(mpl_dates.date2num)
    df = df.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
    return df


# symbol = 'COST'
# df = get_stock_price(symbol)
# df.to_csv('stock.csv')


TICKER = "AAPL"

df = yf.download(TICKER,
                 start="2021-01-01",
                 end="2021-05-30")

# df["Close"].plot(title=f"{TICKER}'s stock price")
df.to_csv('AAPL.csv')
