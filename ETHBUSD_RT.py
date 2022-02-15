from time import sleep
from symtable import Symbol
from binance.client import Client
from binance import BinanceSocketManager
import pandas as pd
import numpy as np
import talib as tl
import csv

api_key = 'DIbFEbRewNALzt0wjXZBkvxVMy7u0rcbOLMrpQZRdR4TK0UMfGks1A3r0qVftPMa'
api_secret = 'Sf2CKtKqJZqN1InO9K0JRhNpXREfqr96rZWOULMuTBOZD5LoimE2I8XLfBmqsC9q'

client = Client(api_key, api_secret)

balance = client.get_account()

bal = balance['balances']

# for b in bal:
#     if float(b['free']) > 0:
#         print(b)

kl = client.get_historical_klines("ETHBUSD", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2017", "1 Feb, 2022")

f = open('1_day_csv', 'w', newline='')

daily_candle_writer = csv.writer(f, delimiter=',')

for day in kl:
    daily_candle_writer.writerow(day)

f.close()