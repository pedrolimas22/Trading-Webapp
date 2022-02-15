from turtle import clear
from binance.client import Client
import csv
# from binance.websockets import BinanceSocketManager
import json

api_key = 'DIbFEbRewNALzt0wjXZBkvxVMy7u0rcbOLMrpQZRdR4TK0UMfGks1A3r0qVftPMa'
api_secret = 'Sf2CKtKqJZqN1InO9K0JRhNpXREfqr96rZWOULMuTBOZD5LoimE2I8XLfBmqsC9q'

client = Client(api_key, api_secret)
prices = client.get_all_tickers()
print(prices)

f = open('all_tickers_csv', 'w', newline='')

all_tickers_writer = csv.writer(f, delimiter=',')

for num1 in prices:
    # for num2 in num1:
    # print(num1["symbol"], num1["price"])
        all_tickers_writer.writerow(num1["symbol"], num1["price"])

f.close()
