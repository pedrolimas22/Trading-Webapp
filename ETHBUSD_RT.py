from symtable import Symbol
from binance.client import Client
import csv

api_key = 'DIbFEbRewNALzt0wjXZBkvxVMy7u0rcbOLMrpQZRdR4TK0UMfGks1A3r0qVftPMa'
api_secret = 'Sf2CKtKqJZqN1InO9K0JRhNpXREfqr96rZWOULMuTBOZD5LoimE2I8XLfBmqsC9q'

client = Client(api_key, api_secret)
print('You' + "'" + 're logged the fuck in My G')

# info = client.get_symbol_info('ETHBUSD')
# trades = client.get_recent_trades()
balance = client.get_account()

bal = balance['balances']

# for b in bal:
#     if float(b['free']) > 0:
#         print(b)

# Getting earliest timestamp availble (on Binance)
earliest_timestamp = client._get_earliest_valid_timestamp('ETHBUSD', '1d')  # Here "ETHUSDT" is a trading pair and "1d" is time interval
print(earliest_timestamp)

# info = client.get_account_snapshot(type='SPOT')

# Getting historical data (candle data or kline)
candle = client.get_klines(symbol='ETHBUSD', interval=Client.KLINE_INTERVAL_4HOUR)
f = open('4hour_csv', 'w', newline='')

candlestrick_writer = csv.writer(f, delimiter=',')

for candlestick in candle:
    print(candlestick)

    candlestrick_writer.writerow(candlestick)

f.close()
# print(candle[1])

# for i in candle:
#     print(i)
