from fastapi.staticfiles import StaticFiles
from web3 import Web3, EthereumTesterProvider
from web3 import Web3, HTTPProvider
import json
from web3.middleware import geth_poa_middleware


#app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)


w3 = Web3(Web3.HTTPProvider('https://eth.getblock.io/rinkeby/?api_key=a8064b26-3884-47bb-92dc-5331a2213e3d'))
#w3.middleware_onion.inject(geth_poa_middleware, layer=0)

abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"}]'


def Gat_bals():
  user_add = input("Ether address: " )
  _trans =  w3.eth.get_balance(user_add)
  _bal2_ = w3.fromWei(_trans, 'ether')
  return _bal2_

print(Gat_bals())

print("sending transactions ....   ...  ... . . . . . . . ")



def send_transactions():
  w3 = Web3(Web3.HTTPProvider('https://eth.getblock.io/rinkeby/?api_key=a8064b26-3884-47bb-92dc-5331a2213e3d'))
  account_1 = input('account_from: ')#'0xF790AAe720e1F24600DDb4632219327c1f4C85eB' # Fill me in
  account_2 = input('account_to: ')#'0xC9A61631F31E2FAaE0f79328A8e30F582C0F6F7d' # Fill me in
  private_key = input('private_key:')#'91ef9b2a36897b331cecfd46b9680885b75253ce742b9fa21e76c6ac26624ff7' # Fill me in

  nonce = w3.eth.getTransactionCount(account_1)

  the_value = input("value: ")

  addr = account_2

  w3.eth.getTransactionCount(addr)
  fee_gas = w3.eth.generate_gas_price()
  print(fee_gas)

  tx = {
      'nonce': nonce,
      'to': account_2,
      'value': w3.toWei(the_value, 'ether'),
      'gas': 2000000,
      'gasPrice': w3.toWei('50', 'gwei'),
      }

  signed_tx = w3.eth.account.sign_transaction(tx, private_key)

  tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

  print(w3.toHex(tx_hash))

  receipt_ = w3.toHex(tx_hash)
print(send_transactions())
print("transactions sent..........")


def transaction_receipt():
  user_tx_hash =   print(w3.toHex(tx_hash))
  _cash = w3.eth.get_transaction_receipt(user_tx_hash)
  #print(_cash)
  return _cash
print(transaction_receipt())



'''@profile
def fetch(contract):
    return contract.functions.getReserves().call()


addr = "0xa37cd29A87975f44b83F06F9BA4D51879a99d378"

with open("abi.json") as f_in:
    abi = json.load(f_in)

client = Web3(Web3.HTTPProvider("https://api.avax.network/ext/bc/C/rpc"))
pair_contract = client.eth.contract(address=client.toChecksumAddress(addr), abi=abi)

while True:
    data = fetch(pair_contract)
    print(data)


#address = '0xc3dbf84Abb494ce5199D5d4D815b10EC29529ff8'
#address = str(input("input address:"))
w3.isConnected()
apis = w3.api
print(apis)
_get_bock = w3.eth.get_block(12345)
#print(_get_bock)
_list_black = w3.eth.get_block('latest')
#print(_list_black)
_chack = w3.eth.block_number
print(_chack)


#bal_ = w3.eth.get_balance('0xC9A61631F31E2FAaE0f79328A8e30F582C0F6F7d')
address = input("input address:") 
_bal_ = w3.eth.get_balance(address)
_bal2_ = w3.fromWei(_bal_, 'ether')

print( _bal2_)

_add_ = input('address:')

checkWallet = Web3.isAddress(_add_)
print(checkWallet)

_id_ = w3.eth.chain_id

print(_id_)

#_trans = w3.eth.get_transaction('0xF790AAe720e1F24600DDb4632219327c1f4C85eB')
#_trans = input("Transaction: ")
#_trans2 = w3.eth.get_transaction(_trans) 
#print(_trans2)


#_cash = w3.eth.get_transaction_receipt('0xF790AAe720e1F24600DDb4632219327c1f4C85eB')
#print(_cash)



#simple example (Web3.py and / or client determines gas and fees, typically defaults to a dynamic fee transaction post London fork)
w3.eth.send_transaction({
  'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
  'from': w3.eth.coinbase,
  'value': 12345
})

# Dynamic fee transaction, introduced by EIP-1559:
HexBytes('0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331')
w3.eth.send_transaction({
  'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
  'from': web3.eth.coinbase,
  'value': 12345,
  'gas': 21000,
  'maxFeePerGas': web3.toWei(250, 'gwei'),
  'maxPriorityFeePerGas': web3.toWei(2, 'gwei'),
})
HexBytes('0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331')

# Legacy transaction (less efficient)
HexBytes('0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331')
w3.eth.send_transaction({
  'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
  'from': w3.eth.coinbase,
  'value': 12345,
  'gas': 21000,
  'gasPrice': web3.toWei(50, 'gwei'),
})
HexBytes('0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331')





def tran():
    buildTransaction({'chainId': 4, 
                   'gas':70000, 
                   'nonce': w3.eth.getTransactionCount(my_account._address)})

def create_acc():
    my_account = w3.eth.account.create('Nobody expects the Spanish Inquisition!')
    print(my_account._address)
    print(my_account._private_key)

abi = json.loads(abi)
dai = w3.eth.contract(address=address, abi=abi)
dai.functions.totalSupply().call()
#print(dai2)
address: w3.eth.getTransactionCount(ETHEREUM_ADDRESS)
signed_txn = w3.eth.account.signTransaction(transaction, '0x265434629c3d2e652550d62225adcb2813d3ac32c6e07c8c39b5cc1efbca18b3')

txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
def create_acc():
    my_account = w3.eth.account.create('Nobody expects the Spanish Inquisition!')
    print(my_account._address)
    print(my_account._private_key)

#print(txn_hash)
'''
