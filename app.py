from crypt import methods
from flask import Flask, redirect, render_template, redirect, flash, jsonify
from symtable import Symbol
from binance.client import Client
from get_data import client, wallet_eur_value, tkn_ticker, tkn_spot_array, tkn_pr_array, tkn_price_eur_array # Importar variáveis utilizadas noutro script
from binance import BinanceSocketManager
from binance import BinanceSocketManager
from jinja2 import Environment, PackageLoader, select_autoescape
import json

# Funções para direcionar a app no URL

app = Flask(__name__)
app.secret_key = b'qweqdasdasdqwqwdas'

@app.route('/')
def index():
    info = client.get_account()
    balances = info['balances']    
    
    return render_template('index.html', my_balances=balances, my_wallet=wallet_eur_value, my_tkn_tick=tkn_ticker, my_tkn_pr_spot=zip(tkn_ticker, tkn_pr_array, tkn_spot_array,tkn_price_eur_array ))

@app.route('/buy', methods=['POST'])
def buy():
    try:
        order = client.create_order(
            side = SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=0.3
        )
    except Exception as e:
        flash(e.message, "error")

    return redirect('/') # Redirecionar para a página principal

@app.route('/history')
def history():
    candlesticks = client.get_historical_klines('ETHBUSD',Client.KLINE_INTERVAL_4HOUR, "22 Mar, 2020", "13 Feb, 2022")

    processed_candlesticks=[]

    for data in candlesticks:
        candlestick = {
            "time": data[0],
            "open": data[1],
            "high": data[2] ,
            "low": data[3],
            "close": data[4]
        }

        processed_candlesticks.append(candlestick)

    return jsonify(processed_candlesticks)