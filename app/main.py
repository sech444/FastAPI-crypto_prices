# -*- coding: utf-8 -*-
#from datetime import datetime, timedelta
from web3 import Web3, EthereumTesterProvider,HTTPProvider
from uuid import uuid4
from fastapi.params import Body
from pydantic import BaseModel 
from fastapi.security import OAuth2PasswordBearer
#from sqlalchemy.orm import Session
#from ethereumweb3 import Get_bals , send_transactions, transaction_receipt
from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form
import json
import requests
from array import *

#webhook_url = "https://webhook.site/efac6181-8311-4cd1-86f3-c7a45f2b1a04"

#app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
# print("7dbec09e214cab2b4f77636cd082c65f85442d0ea65a59c28aa177158c4fe0c0")

w3 = Web3(Web3.HTTPProvider('https://eth.getblock.io/rinkeby/?api_key=a8064b26-3884-47bb-92dc-5331a2213e3d'))
#w3.middleware_onion.inject(geth_poa_middleware, layer=0)

abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"}]'


app = FastAPI()

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


@app.get('/btcusd')
async def index(background_tasks: BackgroundTasks):
    background_tasks.add_task(main)
    return {
        "coin": "BTC",
        "name": "Bitcoin",
        "rate": get_price("bitcoin"),
        "coin_logo": "assets\/img\/xlm.png"
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
        "coin_logo": "assets\/img\/xlm.png"
    }


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


@app.get('/api/v1/xlmusd')
async def index_xlmusd(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_bch)
    return {
        "coin": "XLM",
        "name": "Stellar",
        "rate": getXlmucoinPrice("xlmusd"),
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
        "coin_logo": "assets\/img\/xlm.png"
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
        "coin": "ltc",
        "name": "Litecoin",
        "rate": getDashcoinPrice("crypto_dash"),
        "coin_logo": "assets\/img\/xlm.png"
    }



@app.post("/get_bals")
async def Get_bals(background_tasks: BackgroundTasks,user_adr: str = Form(...)):
    background_tasks.add_task(Get_bals(user_adr))
    try:
        _trans = w3.eth.get_balance(user_adr)
        _bal2_ = w3.fromWei(_trans, 'ether')
        return {"_bal2_": _bal2_}
    except:
        {'data':"Invalid_wallet" }




@app.post("/api/tarnsaction")
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
    print(new_data)
    return {"New_tarnsation": new_data , }
   
        

@app.post('/api/tx_hash')
async def transaction_receipt(background_tasks:BackgroundTasks,tx_hash:str = Form(...),webhook_url:str = Form(...)) -> dict():
    
    receipt_ = w3.eth.get_transaction_receipt(tx_hash)
    w3.toJSON(receipt_ )
    print(receipt_)
    data = {
        'acc': 'transaction',
        'details': w3.toJSON(receipt_ ),
    }
    r=requests.post(webhook_url,data=json.dumps(data))

    return {"data" : w3.toJSON(receipt_ )}

   
 


"""@app.get('/')
async def index(background_tasks: BackgroundTasks):
    background_tasks.add_task(main)
    return {
        "coin": "BTC",
        "name": "Bitcoin",
        "rate": get_price("bitcoin"),
        "coin_logo": "assets\/img\/xlm.png
    }  """


listData = [
    {
        "coin": "btc",
        "name": "Bitcoin",
        "rate": get_price("bitcoin"),
        "coin_logo": "assets\/img\/bch.png"
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
        "coin": "dash",
        "name": "dash",
        "rate": getDashcoinPrice("crypto_dash"),
        "coin_logo": "assets\/img\/dash.png"
    },
    {
        "coin": "xlm",
        "name": "Stellar",
        "rate": getXlmucoinPrice("stellar"),
        "coin_logo": "assets\/img\/xlm.png"
    }
]

"""
sechmos
"""
