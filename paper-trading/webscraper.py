from bs4 import BeautifulSoup
import requests
import AI
kolscan_leaderboard = "https://kolscan.io/leaderboard"

def topWallets():
    #use gmgn api
    top_kolscan = kolscanLeaders()
    return None

def gmgnLeaders():
    return None
    
def kolscanLeaders():
    print("test")
    request = requests.get(kolscan_leaderboard)
    parsedHTML = BeautifulSoup(request.content, 'html.parser').prettify()
    leaders = dissectContent(parsedHTML, "given the following content return only just a json json with the top ten trader name, solana wallet address,  win loss rate,  pnl, and wallet balance:")
    return leaders


def dissectContent(content, prompt):
    question = prompt + content 
    AI.providePrompt(prompt)
    return None
 


#schema for json:
#name , wallet address, win rate , pnl, and wallet balance