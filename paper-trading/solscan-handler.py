import requests
from solana.rpc.api import Client
from solders.pubkey import Pubkey

rpc = "https://solana.drpc.org/"
dexscreener_limit_pm = 60

client = Client(rpc)

def solanPrice():
    return None


def token_holdings(wallet_address):
    params = rpc_params(wallet_address)
    request = requests.post(rpc, json=params)
    limit_tracker = 0
    if (request.status_code == 200):
        response = request.json()
        #this how we get to specific key value in a json object just use the array symbol and add the string name of the key to it
        holdings_obtained = response['result']['value']
        print(type(holdings_obtained))
        count = 0
        #since its a list we only loop like this if its a dict type we use holdings_obtained.list() and use key, value
        for  value in holdings_obtained:
            current_holding = value['account']['data']['parsed']['info']
            token_held = current_holding['mint']
            
            amount_held = current_holding['tokenAmount']['amount']
       
            if (amount_held != '0' and limit_tracker != 60):
                 token_data = token_info(token_held)
                 limit_tracker += 1
                # print(f"Holding CA: {token_held}, Amount: {amount_held}")
               
        
    return None

def token_info(mint_address):
    request = requests.get(f"https://api.dexscreener.com/token-pairs/v1/solana/{mint_address}")
    response = request.json()
    for key in response:
        name = key['baseToken']['name']
        price = key['priceUsd']
        marketcap = key['marketCap']
        print(f"INFO: {name} , mc: {marketcap}, price: {price}")
    return None


def rpc_params(wallet_address):
    return  {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getTokenAccountsByOwner",
    "params": [
        wallet_address,
        {"programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"},  # Token Program ID
        {"encoding": "jsonParsed"}
    ]
}


token_holdings("CRVidEDtEUTYZisCxBZkpELzhQc9eauMLR3FWg74tReL")