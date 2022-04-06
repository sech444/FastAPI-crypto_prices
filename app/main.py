# -*- coding: utf-8 -*-
#from datetime import datetime, timedelta
from web3 import Web3, EthereumTesterProvider,HTTPProvider
from uuid import uuid4
from fastapi.params import Body
from pydantic import BaseModel 
#from bitcoinlib.wallets import Wallet, wallet_delete
from bitcoinlib.mnemonic import Mnemonic
from random import randrange
from fastapi.security import OAuth2PasswordBearer
import secrets
from eth_account import Account
import time
import hmac
import hashlib
from urllib.parse import urljoin, urlencode
from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form
import json
import requests
from array import *
from bitcoin import *
from dotenv import load_dotenv
import os 


load_dotenv()
API_KEY = os.getenv("ID")
SECRET_KEY = os.getenv("SECRET_KEY")
BASE_URL = 'https://api.binance.com'

headers = {
    'X-MBX-APIKEY': API_KEY
}


#webhook_url = "https://webhook.site/efac6181-8311-4cd1-86f3-c7a45f2b1a04"

#app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

w3 = Web3(Web3.HTTPProvider('https://eth.getblock.io/rinkeby/?api_key=a8064b26-3884-47bb-92dc-5331a2213e3d'))
#w3.middleware_onion.inject(geth_poa_middleware, layer=0)

abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"}]'

app = FastAPI()
#client = Client(api_key="I4E8iZwBV6LiN5MVrnSjtiJaTfDdpA7rC7wzooPv3B9W0TOBpshxP4KK0JKPKmhe", api_secret="vsmABNkdw68D8J5viqi7vkzWt9pnjbPuxAhCjtPqP83swrD7UdmZgsUMtCB2jmIt")

#webhook_url = "https://webhook.site/36f9ce75-d60c-4e1c-b148-dee920cfca4f"

'''
db: List[User] = [
    Users(
    id= uuid4 (),
    frist_name = "James",
    last_name = "Jamila",
    middle_name = None,
    gender = Gender.female,
    ),
     User(
    id= uuid4 (),
    frist_name = "James",
    last_name = "Jamila",
    middle_name = None,
    gender = Gender.female,
    )
]'''
class Tx_user(BaseModel):
    account_from: int = Body(None)
    account_to: int = Body(None)
    value_to_send: float = Body(None)
    private_key: int = Body(None)

@app.get("/")
def root():
    return listData


def get_price(crypto):
    URL = 'https://www.bitstamp.net/api/ticker/btcusd/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")


def main():
    last_price = -1

    while True:

        crypto = 'bitcoin'
        price = get_price(crypto)

        if price != last_price:
           # print('Bitcoin price: ',price)
            last_price = price
    return


@app.get('/api/v1/btcusd')
async def index(background_tasks: BackgroundTasks):
    background_tasks.add_task(main)
    return {
        "coin": "BTC",
        "name": "Bitcoin",
        "rate": get_price("bitcoin"),
        "coin_logo": "assets\/img\/btc.png"
    }


def get_price_bch(crypto_bchusd):
    URL = 'https://www.bitstamp.net/api/v2/ticker/bchusd/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")


def main_bch():
    last_price = -1

    while True:

        crypto_bchusd = 'bitcoin_cash'
        price = get_price_bch(crypto_bchusd)

        if price != last_price:
           # print('Bitcoin price: ',price)
            last_price = price
    return


@app.get('/api/v1/bch')
async def index_bch(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_bch)
    return {
        "coin": "BCH",
        "name": "Bitcoin Cash",
        "rate": get_price_bch("bitcoin_cash"),
        "coin_logo": "assets\/img\/bch.png"
    }

"""
def getXlmucoinPrice(crypto_xlmusd):
    URL = 'https://www.bitstamp.net/api/v2/ticker/xlmusd/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")


def main_xlmusd():
    last_price = -1

    while True:

        crypto_xlmusd = 'xlmusd'
        price = getXlmucoinPrice(crypto_xlmusd)

        if price != last_price:
           # print('Bitcoin price: ',price)
            last_price = price
    return



@app.get('/api/v1/bch')
async def index_bch(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_bch)
    return {
        "coin": "BCH",
        "name": "Bitcoin Cash",
        "rate": get_price_bch("bitcoin_cash"),
        "coin_logo": "assets\/img\/bch.png"
    }
"""

def getethercoinPrice(crypto_ether):
    URL = 'https://www.bitstamp.net/api/v2/ticker/ethusd/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")


def main_ether():
    last_price = -1

    while True:

        crypto_ether = 'ether'
        price = getethercoinPrice(crypto_ether)

        if price != last_price:
           # print('Bitcoin price: ',price)
            last_price = price
    return


@app.get('/api/v1/ethusd')
async def index_ether(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_ether)
    return {
        "coin": "ether",
        "name": "Ethereum",
        "rate": getethercoinPrice("ether"),
        "coin_logo": "assets\/img\/ether.png"
    }


def getXlmcoinPrice(crypto_xlmusd):
    URL = 'https://www.bitstamp.net/api/v2/ticker/xlmusd/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying xlmusd")


def main_Xlmusd():
    last_price = -1

    while True:

        crypto_xlmusd = 'Stellar'
        price = getXlmcoinPrice(crypto_xlmusd)

        if price != last_price:
           # print('Bitcoin price: ',price)
            last_price = price
    return


@app.get('/api/v1/xlmusd')
async def index_Stellar(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_Xlmusd)
    return {
        "coin": "xlm",
        "name": "Stellar",
        "rate": getXlmucoinPrice("stellar"),
        "coin_logo": "assets\/img\/xlm.png"
    }





def getLtccoinPrice(crypto_ltc):
    URL = 'https://www.bitstamp.net/api/v2/ticker/ltcusd/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")


def main_ltc():
    last_price = -1

    while True:

        crypto_ltc = 'litecoin'
        price = getLtccoinPrice(crypto_ltc)

        if price != last_price:
           # print('Bitcoin price: ',price)
            last_price = price
    return


@app.get('/api/v1/ltc')
async def index_ltc(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_ltc)
    return {
        "coin": "ltc",
        "name": "Litecoin",
        "rate": getLtccoinPrice('litercoin'),
        "coin_logo": "assets\/img\/ltc.png"
    }
    

def getxrpusdrice(crypto_xrpusd):
    URL = 'https://www.bitstamp.net/api/v2/ticker/xrpusd/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")


def main_xrp():
    last_price = -1

    while True:

        crypto_xrp = 'Ripple'
        price = getxrpusdrice(crypto_xrpusd)
        if price != last_price:
           # print('Bitcoin price: ',price)
            last_price = price
    return


@app.get('/api/v1/xrpusd')
async def index_xrp(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_xrp)
    return {
        "coin": "xrp",
        "name": "Proton",
        "rate": getxrpusdPrice("Ripple"),
        "coin_logo": "assets\/img\/xrp.png"
    }
   
    
    


def getDashcoinPrice(crypto_dash):
    URL = 'https://www.dashcentral.org/api/v1/public'
    try:
        r = requests.get(URL)
        priceFloat = json.loads(r.text)
        #ans = json.loads(priceFloat)
        # print(priceFloat)
        data = (priceFloat['exchange_rates'])
    except requests.ConnectionError:
        print("Error querying Bitstamp API")
    return data['dash_usd']
# print('Dash:',getDashcoinPrice(crypto_dash))


def main_dash():
    last_price = -1

    while True:

        crypto_dash = 'dash'
        price = getDashcoinPrice(crypto_dash)

        if price != last_price:
            #print('Dashcoin price: ',price)
            last_price = price
    return
# print(main_xlmusd())


@app.get('/api/v1/dash')
async def index_dash(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_dash)
    return {
        "coin": "dash",
        "name": "Dash",
        "rate": float(getDashcoinPrice("crypto_dash")),
        "coin_logo": "assets\/img\/dash.png"
    }



@app.post("/api/v1/get_ether_bals")
async def Get_ether_bals(user_adr: str = Form(...)):
    #background_tasks.add_task(Get_bals(user_adr))
    try:
        _trans = w3.eth.get_balance(user_adr)
        _bal2_ = w3.fromWei(_trans, 'ether')
        return {"_bal2_": _bal2_}
    except:
        {'data':"Invalid_wallet" }




@app.post("/api/v1/tarnsaction")
async def tarnsaction(background_tasks:BackgroundTasks,account_from:str = Form(...), account_to: str = Form(...),value_to_send: float=Form(...), private_key: str=Form(...)):
    account_1 = account_from 
    account_2 = account_to 
    value    = value_to_send  
                          
    private_key = private_key  
    addr = account_2
     
    nonce = w3.eth.getTransactionCount(account_1)

    tx = {
                    'nonce': nonce,
                    'to': account_2,
                    'value': w3.toWei(value, 'ether'),
                    'gas': 200000,
                    'gasPrice': w3.toWei('50', 'gwei'),
                }
        
        


    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash =  w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    new_data= (w3.toHex(tx_hash))
    return {"New_tarnsation": new_data , }
   
        

@app.post('/api/v1/api/tx_hash')
async def transaction_receipt(background_tasks:BackgroundTasks,tx_hash:str = Form(...),webhook_url:str = Form(...)) -> dict():
    receipt_ = w3.eth.get_transaction_receipt(tx_hash)
    w3.toJSON(receipt_ )
    data = {
        'acc': 'transaction',
        'details': w3.toJSON(receipt_ ),
    }
    r=requests.post(webhook_url,data=json.dumps(data))

    return {"data" : w3.toJSON(receipt_ )}

@app.get('/api/v1/api/ether_wallet')
async def eth_wallet():
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    return{"private_key": private_key,
           "address": acct.address}



@app.get('/api/v1/api/btc_wallet')
async def bitcoin_wallet():
    private_key = random_key()
    pubilc_key = privtopub(private_key)
    address = pubtoaddr(pubilc_key)
    
    return {"private_key":private_key,
            "pubilc_key": pubilc_key,
            "address" :  address
             }



 
def getbnbusdtprice(Binance_Coin):
    base_url = "https://api.binance.com"
    path = "/api/v3/ticker/price"
    params = '?symbol=BNBUSDT'
    try:
        r = requests.get(base_url+path+params)
        data = r.json()
        priceFloat = float(data['price'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")  


def gettrxusdtprice(tron_Coin):
    base_url = "https://api.binance.com"
    path = "/api/v3/ticker/price"
    params = '?symbol=TRXUSDT'
    try:
        r = requests.get(base_url+path+params)
        data = r.json()
        priceFloat = float(data['price'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")  



@app.get('/api/v1/bnbusdt')
def binance_BNBUSDT():
    base_url = "https://api.binance.com"
    path = "/api/v3/ticker/price"
    params = '?symbol=BNBUSDT'
    r = requests.get(base_url+path+params)
    data = r.json()
    return {
        "coin": "BNB",
        "name": "Binance Coin",
        "rate_usdt": float(data['price']),
        "coin_logo": "assets\/img\/bnb.png"
    }


@app.get('/api/v1/trxusdt')
def binance_TRXUSDT():
    base_url = "https://api.binance.com"
    path = "/api/v3/ticker/price"
    params = '?symbol=TRXUSDT'
    r = requests.get(base_url+path+params)
    data = r.json()
    return {
        "coin": "TRX",
        "name": "TRON Coin",
        "rate_usdt": float(data['price']),
        "coin_logo": "assets\/img\/trx.png"
    }
    
    
@app.get('/api/v1/btcusdt')
def binance_BTCUSDT():
    base_url = "https://api.binance.com"
    path = "/api/v3/ticker/price"
    params = '?symbol=BTCUSDT'
    r = requests.get(base_url+path+params)
    data = r.json()
    return {
        "coin": "BTC",
        "name": "Bitcoin",
        "rate_usdt": float(data['price']),
        "coin_logo": "assets\/img\/btcusdt.png"
    }    


@app.get("/api/v1/all_coin_binance")
def all_coin():
    PATH = '/api/v3/ticker/price'
    base_url = "https://api.binance.com"
    params = {
        'symbol': 'BTCUSDT'
    }

   #url = urljoin(base_url, PATH)
    r = requests.get(base_url+ PATH)
    if r.status_code == 200:
        data = r.json()
        json_formatted_str = json.dumps(data, indent=4)
    else:
        raise BinanceException(status_code=r.status_code, data=r.json())
    
    return{"coins" : json_formatted_str}

@app.post("/api/v1/create_Order")
def create_Order(symbol: str = Form(...),buy_or_sell: str = Form(...),quantity: float = Form(...)):
    PATH = '/api/v3/order'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol.upper(),
        'side': buy_or_sell.upper(),
        'type': 'MARKET',
        'quantity': quantity,
        'timestamp': timestamp
    }

    query_string = urlencode(params)
    params['signature'] = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    url = urljoin(BASE_URL, PATH)
    r = requests.post(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        print(data)
    else:
        print(EnvironmentError)
        #raise BinanceException(status_code=r.status_code, data=r.json())
    return{"data" : json.dumps(data, indent=2)}

    

listData = [
    {
        "coin": "btc",
        "name": "Bitcoin",
        "rate": get_price("bitcoin"),
        "coin_logo": "assets\/img\/btc.png"
    },
    {
        "coin": "bch",
        "name": "Bitcoin Cash",
        "rate": get_price_bch("bitcoin_cash"),
        "coin_logo": "assets\/img\/bch.png"
    },
    {
        "coin": "ltc",
        "name": "Litecoin",
        "rate": getLtccoinPrice('litercoin'),
        "coin_logo": "assets\/img\/ltc.png"
    },
    {
        "coin": "xrp",
        "name": "Ripple",
        "rate": getxrpusdrice("Ripple"),
        "coin_logo": "assets\/img\/xrp.png"
    },
    {
        "coin": "dash",
        "name": "dash",
        "rate": getDashcoinPrice("crypto_dash"),
        "coin_logo": "assets\/img\/dash.png"
    },
    {
        "coin": "xlm",
        "name": "Stellar",
        "rate": getXlmcoinPrice("crypto_xlmusd"),
        "coin_logo": "assets\/img\/xlm.png"
    },
    {
        "coin": "ether",
        "name": "Ethereum",
        "rate": getethercoinPrice("ether"),
        "coin_logo": "assets\/img\/ether.png"
    },
    {
        "coin": "BNB",
        "name": "Binance Coin",
        "rate": getbnbusdtprice("Binance_Coin"),
        "coin_logo": "assets\/img\/bnb.png"
    
    },
    {
        "coin": "TXR",
        "name": "TRON Coin",
        "rate": gettrxusdtprice("tron_Coin"),
        "coin_logo": "assets\/img\/txr.png"
    
    }
]
