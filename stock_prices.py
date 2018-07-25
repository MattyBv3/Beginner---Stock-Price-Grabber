# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 20:52:10 2018

@author: Pr1d3sP4ran01a
"""

import datetime as dt
# matplotlib for data visualization / to graph things
import matplotlib.pyplot as plt
from matplotlib import style
# pandas for data analysis / to manipulate data
import pandas as pd
# pandas_data... = newest io library atm
import pandas_datareader.data as web

# set style for pretty graphs - sexy charts = proft
style.use('ggplot')
#set date range of stock prices to grab
start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

# MB test
ticker = input("Type a stock ticker: ")
# MB test

# make dataframe from stock history data (dataframe = spreadsheet or database table held in RAM)
# web.DataReader... = uses pandas_datareader pkg, looks for ticker "TSLA", gets info from morningstar, etc.
df = web.DataReader(ticker, 'morningstar', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

# save DataFrame to .csv file
df.to_csv('stock_ticker_output.csv')
# read data from .csv file rather than Yahoo api
df = pd.read_csv('stock_ticker_output.csv', parse_dates=True, index_col=0)
# graph it with
df.plot()
plt.show()
# so far just shows volume, now to graph what we're interested in
# plots 2nd graph showing highs & lows after volume
df[['High','Low']].plot()
plt.show()
# can't get 'Adj Close' to work https://pythonprogramming.net/handling-stock-data-graphing-python-programming-for-finance/?completed=/getting-stock-prices-python-programming-for-finance/
# solution, use 'Close' instead of 'Adj Close'
df['Close'].plot()
plt.show()

# moving average
# creates (or re-writes if already exists) column df['100ma']
# stating that df['100ma'] column = 'Close" column w/ rolling method applied, with window of 100, and 
# this window will be an average (mean)
df['100ma'] = df['Close'].rolling(window=100).mean()
print(df.head())



# .head() is Pandas DataFrames feature / will output the first n rows, if no n chosen, default = 5
print(df.head())
