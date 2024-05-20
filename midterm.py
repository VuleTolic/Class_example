import matplotlib
from matplotlib import pylab as plt
import pandas as pd
import pandas_datareader.data as web
import datetime
import yfinance as yfin
yfin.pdr_override()

today = datetime.datetime.today()
formatted_date = today.strftime("%Y-%m-%d")
df1 = web.DataReader('TSLA', start='2024-02-15', end=formatted_date)
df1.index = pd.to_datetime(df1.index)

