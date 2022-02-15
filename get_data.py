from turtle import clear
from binance.client import Client
# from binance.websockets import BinanceSocketManager
import json

api_key = 'DIbFEbRewNALzt0wjXZBkvxVMy7u0rcbOLMrpQZRdR4TK0UMfGks1A3r0qVftPMa'
api_secret = 'Sf2CKtKqJZqN1InO9K0JRhNpXREfqr96rZWOULMuTBOZD5LoimE2I8XLfBmqsC9q'

client = Client(api_key, api_secret)

trade_pair = 'eurbusd'
interval = '1m'

socket = 'wss://stream.binance.com:9443/ws/eurbusd@aggtrade'


status = client.get_account()


price_EURBUSD = client.get_klines(symbol='EURBUSD', interval=Client.KLINE_INTERVAL_1MINUTE)
price_ADABUSD = client.get_klines(symbol='ADABUSD', interval=Client.KLINE_INTERVAL_1MINUTE)
price_AUDIOBUSD = client.get_klines(symbol='AUDIOBUSD', interval=Client.KLINE_INTERVAL_1MINUTE)
price_AVAXBUSD = client.get_klines(symbol='AVAXBUSD', interval=Client.KLINE_INTERVAL_1MINUTE)
price_BNBBUSD = client.get_klines(symbol='BNBBUSD', interval=Client.KLINE_INTERVAL_1MINUTE)
price_DOTBUSD = client.get_klines(symbol='DOTBUSD', interval=Client.KLINE_INTERVAL_1MINUTE)
price_ETHBUSD = client.get_klines(symbol='ETHBUSD', interval=Client.KLINE_INTERVAL_1MINUTE)
price_GALABUSD = client.get_klines(symbol='GALABUSD', interval=Client.KLINE_INTERVAL_1MINUTE)
price_HNTBUSD = client.get_klines(symbol='HNTBUSD', interval=Client.KLINE_INTERVAL_1MINUTE)
price_LUNABUSD = client.get_klines(symbol='LUNABUSD', interval=Client.KLINE_INTERVAL_1MINUTE)
price_MANABUSD = client.get_klines(symbol='MANABUSD', interval=Client.KLINE_INTERVAL_1MINUTE)
price_MATICBUSD = client.get_klines(symbol='MATICBUSD', interval=Client.KLINE_INTERVAL_1MINUTE)
price_ONEBUSD = client.get_klines(symbol='ONEBUSD', interval=Client.KLINE_INTERVAL_1MINUTE)
price_SANDBUSD = client.get_klines(symbol='SANDBUSD', interval=Client.KLINE_INTERVAL_1MINUTE)
price_SOLBUSD = client.get_klines(symbol='SOLBUSD', interval=Client.KLINE_INTERVAL_1MINUTE)

price_EURBUSD = price_EURBUSD[0]
price_EURBUSD = float(price_EURBUSD[1])

price_ADABUSD = price_ADABUSD[0]
price_ADABUSD = float(price_ADABUSD[1])
price_ADA = round(price_ADABUSD/price_EURBUSD,2)
# print('ADA: ' + str(price_ADA))

price_AUDIOBUSD = price_AUDIOBUSD[0]
price_AUDIOBUSD = float(price_AUDIOBUSD[1])
price_AUDIO = round(price_AUDIOBUSD/price_EURBUSD,2)
# print('AUDIO: ' + str(price_AUDIO))

price_AVAXBUSD = price_AVAXBUSD[0]
price_AVAXBUSD = float(price_AVAXBUSD[1])
price_AVAX = round(price_AVAXBUSD/price_EURBUSD,2)
# print('AVAX: ' + str(price_AVAX))

price_BNBBUSD = price_BNBBUSD[0]
price_BNBBUSD = float(price_BNBBUSD[1])
price_BNB = round(price_BNBBUSD/price_EURBUSD,2)
# print('BNB: ' + str(price_BNBBUSD))

price_DOTBUSD = price_DOTBUSD[0]
price_DOTBUSD = float(price_DOTBUSD[1])
price_DOT = round(price_DOTBUSD/price_EURBUSD,2)
# print('DOT: ' + str(price_DOTBUSD))

price_ETHBUSD = price_ETHBUSD[0]
price_ETHBUSD = float(price_ETHBUSD[1])
price_ETH = round(price_ETHBUSD/price_EURBUSD,2)
# print('ETH: ' + str(price_ETH))

price_GALABUSD = price_GALABUSD[0]
price_GALABUSD = float(price_GALABUSD[1])
price_GALA = round(price_GALABUSD/price_EURBUSD,2)
# print('GALA:' + str(price_GALA))
 
price_HNTBUSD = price_HNTBUSD[0]
price_HNTBUSD = float(price_HNTBUSD[1])
price_HNT = round(price_HNTBUSD/price_EURBUSD,2)
# print('HNT: ' + str(price_HNT))

price_LUNABUSD = price_LUNABUSD[0]
price_LUNABUSD = float(price_LUNABUSD[1])
price_LUNA = round(price_LUNABUSD/price_EURBUSD,2)
# print('LUNA: ' + str(price_LUNA))

price_MANABUSD = price_MANABUSD[0]
price_MANABUSD = float(price_MANABUSD[1])
price_MANA = round(price_MANABUSD/price_EURBUSD,2)
# print('MANA: ' + str(price_MANA))

price_MATICBUSD = price_MATICBUSD[0]
price_MATICBUSD = float(price_MATICBUSD[1])
price_MATIC = round(price_MATICBUSD/price_EURBUSD,2)
# print('MATIC: ' + str(price_MATIC))

price_ONEBUSD = price_ONEBUSD[0]
price_ONEBUSD = float(price_ONEBUSD[1])
price_ONE = round(price_ONEBUSD/price_EURBUSD,2)
# print('ONE: ' + str(price_ONE))

price_SANDBUSD = price_SANDBUSD[0]
price_SANDBUSD = float(price_SANDBUSD[1])
price_SAND = round(price_SANDBUSD/price_EURBUSD,2)
# print('SAND: ' + str(price_SAND))

price_SOLBUSD = price_SOLBUSD[0]
price_SOLBUSD = float(price_SOLBUSD[1])
price_SOL = round(price_SOLBUSD/price_EURBUSD,2)
# print('SOL: ' + str(price_SOL))

tkn_pr_array = [price_ADA, price_AUDIO, price_AVAX, price_BNB, price_DOT, price_ETH, price_GALA, price_HNT, price_LUNA, price_MANA, price_MATIC, price_ONE, price_SAND, price_SOL]
tkn_spot_array = []
tkn_price_eur_array = []
# price_EURBUSD = client.get_symbol_info('EURBUSD')

info = client.get_account_snapshot(type='SPOT') # It's a dictionary
info_1 = info['snapshotVos']
spot_info = info_1[2]
data = spot_info['data'] 
balance = data['balances']

# print(len(balance))

for i in balance: # Go over the length of all token prices array
    if i['free'] != '0': 
        tkn_spot_array.append(float(i['free']))

for num1, num2 in zip(tkn_spot_array, tkn_pr_array):
    spot_token_value = 0
    spot_token_value = num1 * num2
    tkn_price_eur_array.append(spot_token_value)

print(tkn_pr_array)
print(len(tkn_pr_array))
print(type(tkn_pr_array[0]))
print(tkn_spot_array)   
print(len(tkn_spot_array))  
print(type(tkn_spot_array[0]))    
print(tkn_price_eur_array)  
# print(sum(tkn_price_eur_array))     

wallet_eur_value = round(sum(tkn_price_eur_array),2) 
print(wallet_eur_value)
# # Getting historical data (candle data or kline)
# candle = client.get_klines(symbol='ETHBUSD', interval=Client.KLINE_INTERVAL_4HOUR)
# f = open('4hour_csv', 'w', newline='')

# candlestrick_writer = csv.writer(f, delimiter=',')

# for candlestick in candle:
#     print(candlestick)

#     candlestrick_writer.writerow(candlestick)

# f.close()