import yfinance as yf   #yahoo finance API for candles
import pandas as pd     #formatting/datasets library
import pytz             #timezone library
from datetime import datetime, date, timedelta

# timezone adjust
now = datetime.now(pytz.timezone("US/Eastern"))

print("Now in US/East:", now)
today = date.today()


ticker = "QQQ"   #title BEING CALLED
bar= yf.download(ticker, start=(today - timedelta(1)), end=today, interval="5m") #call for  5-minutes candle of yesterday of said title

#data printer
print(bar.head())  # First 5 rows (bars from market open)
print(bar.tail())  # Last 5 rows (toward market close)
