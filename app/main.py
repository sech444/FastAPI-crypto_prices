# -*- coding: utf-8 -*-
#from datetime import datetime, timedelta
from web3 import Web3, EthereumTesterProvider,HTTPProvider
from uuid import uuid4
from fastapi.params import Body
from pydantic import BaseModel 
from bitcoinlib.wallets import Wallet, wallet_delete
from bitcoinlib.mnemonic import Mnemonic
from random import randrange
from fastapi.security import OAuth2PasswordBearer
import secrets
from eth_account import Account
from pywallet import wallet
#from ethereumweb3 import Get_bals , send_transactions, transaction_receipt
from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form
import json
import requests
from array import *
from bitcoin import *

#webhook_url = "https://webhook.site/efac6181-8311-4cd1-86f3-c7a45f2b1a04"

#app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

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



@app.get('/api/v1/bch')
async def index_bch(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_bch)
    return {
        "coin": "BCH",
        "name": "Bitcoin Cash",
        "rate": get_price_bch("bitcoin_cash"),
        "coin_logo": "assets\/img\/xlm.png"
    }


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
        "coin_logo": "assets\/img\/xlm.png"
    }


def getXlmcoinPrice(crypto_xlmusd):
    URL = 'https://www.bitstamp.net/api/v2/ticker/xlmusd/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API xlmusd")


def main_Xlm():
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
    background_tasks.add_task(main_xlm)
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
        "coin_logo": "assets\/img\/xlm.png"
    }
    

def getxrpusdPrice(crypto_xrpusd):
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

        crypto_xrp = 'Proton'
        price = getLtccoinPrice(crypto_xrp)

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
        "rate": getxrpusdPrice("Proton"),
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

@app.get('/api/v1/eth_wallet')
async def eth_wallet():
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    return{"private_key": private_key,
           "Address": acct.address}



@app.get('/api/btc_wallet')
async def bitcoin_wallet():
    private_key = random_key()
    pubilc_key = privtopub(private_key)
    address = pubtoaddr(pubilc_key)
    
    return {"private_key":private_key,
            "pubilc_key": pubilc_key,
            "address" :  address
             }



# This library simplify the process of creating new wallets for the BTC, BTG, BCH, ETH, LTC, DASH and DOGE 

# generate 12 word mnemonic seed
@app.get('/api/LTC_wallet')
async def Litecoin_wallet() -> dict():
    seed = wallet.generate_mnemonic()

    # create litecoin wallet
    w = wallet.create_wallet(network="LTC", seed=seed)
    data = w
    
    return{"public_key" : data["public_key"],
           "seed"     : seed,
           "Litecoin_wallet" : data["address"],
           "private_key"  : data["private_key"],
           "xprivate_key" : data["xprivate_key"],
           "xpublic_key"  : data["xpublic_key"],
           "children"  : data["children"],
           }

@app.get('/api/BTC_HD_wallet')
async def BTC_HD__wallet() -> dict():
    seed = wallet.generate_mnemonic()

    # create BTC_HD_ wallet
    w = wallet.create_wallet(network="BTC", seed=seed)
    data = w
    
    return{"public_key" : data["public_key"],
           "seed"     : seed,
           "BTC_HD__wallet" : data["address"],
           "private_key"  : data["private_key"],
           "xprivate_key" : data["xprivate_key"],
           "xpublic_key"  : data["xpublic_key"],
           "children"  : data["children"],
           }

@app.get('/api/BCH_wallet')
async def Bitcoin_Cash_wallet() -> dict():
    seed = wallet.generate_mnemonic()

    # create  Bitcoin Cash wallet
    w = wallet.create_wallet(network="BCH", seed=seed)
    data = w
    
    return{"public_key" : data["public_key"],
           "seed"     : seed,
           "Bitcoin_Cash_wallet" : data["address"],
           "private_key"  : data["private_key"],
           "xprivate_key" : data["xprivate_key"],
           "xpublic_key"  : data["xpublic_key"],
           "children"  : data["children"],}
    
    
@app.get('/api/DASH_wallet')
async def DASH_wallet() -> dict():
    seed = wallet.generate_mnemonic()

    # create  DASH wallet
    w = wallet.create_wallet(network="DASH", seed=seed)
    data = w
    
    return{"public_key" : data["public_key"],
           "seed"     : seed,
           "DASH_wallet" : data["address"],
           "private_key"  : data["private_key"],
           "xprivate_key" : data["xprivate_key"],
           "xpublic_key"  : data["xpublic_key"],
           "children"  : data["children"],}
   




    
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
        "coin": "xrp",
        "name": "Proton",
        "rate": getxrpusdPrice("Proton"),
        "coin_logo": "assets\/img\/xlm.png"
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
    },
    {
        "coin": "ether",
        "name": "Ethereum",
        "rate": getethercoinPrice("ether"),
        "coin_logo": "assets\/img\/xlm.png"
    }
]
