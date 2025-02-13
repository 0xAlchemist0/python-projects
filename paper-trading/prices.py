import os

import requests
from dotenv import load_dotenv

load_dotenv()
alchemy = os.getenv("ALCHEMY")

alch_base_url = f"https://api.g.alchemy.com/prices/v1/{alchemy}/tokens/historical"


def historicalPrice(token, start, end, interval):
    request_params = parameters(token, start, end, interval)
    request = requests.post(alch_base_url, json=request_params[0], headers=request_params[1])
    #index 0 payload parameter with timestamp for history
    #index 1 headers with contetn return ype
    print(request.content)
    
    return None


def currentPrice(ticker):
    return None

def parameters(token ,start, end, interval):
    #returns a json array in tuple form which we cannot chnage once made
    return (
         {
        "symbol": token,
        "startTime": start,
        "endTime": end,
        "interval": interval
        }, 
         {
             "accept": "application/json",
             "content-type": "application/json"
         }
    )
    
historicalPrice("sol","2024-01-01T00:00:00Z", 1706745599, "1d")