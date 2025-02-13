import requests
from bs4 import BeautifulSoup

import AI

kolscan_leaderboard = "https://kolscan.io/leaderboard"

def topWallets():
    #use gmgn api
    kolscan_leaderboard = kolscan()
    print(kolscan_leaderboard)
    return kolscan_leaderboard

def gmgnLeaders():
    return None
    
def kolscan():
    request = requests.get(kolscan_leaderboard)
   
    target_content = ('div', 'leaderboard-section','trader-entry' ,10, 'trader-name', 'profit-sol', 'profit-usd')
    leaderboard = dissectContent(request,None, target_content)
    
    return leaderboard


#only when we use AI (not yet do first simple functionalites)
def dissectContent(content, prompt, targets=None):
    if (targets != None):
        output = extractElements(content, targets)
        return output
        
    else:print("ai")
    return None
 
 #setup for json ,name, address,win rate, pnl, 
def extractElements(response, targets):
    #parse the request response so beautiful soup can read
    soup = BeautifulSoup(response.content, 'html.parser')
    #extract out the leaderboard div contains the mapping of all the top traders 
    #it got all we need
    target_elements = soup.find('div', class_='leaderboard_leaderboardContainer__JEv3z')
    output = []
    
    #using the div with all the data we loop through each div of the trader which each div has the class leaderboard_leaderboardUser__8OZpJ
    # we also add div so we only get the div 
    for element in target_elements.find_all('div', class_='leaderboard_leaderboardUser__8OZpJ'):
        #get the name by finding th ea element in the div and extracting the text
         name = element.find('a').text.strip()
        #get the win rate by finding th div  element with the class remove-mobile in the div and extracting the text
         
         win_rate = element.find('div','remove-mobile').text.strip()
        #get the pnl by finding th ea div element in the div witht the class leaderboard_totalProfitNum__HzfFO and extracting the text
         
         pnl_sol = element.find('div', 'leaderboard_totalProfitNum__HzfFO').text.strip()
           #get the address by finding th ea a element in the div wand extracting the value link from the href
         address = element.find('a').get('href').replace("/account/", "")
    
         output.append({"name": name,"address":address ,"winrate": win_rate, "pnl": pnl_sol})
    
    return output
    


topWallets()


#schema for json:
#name , wallet address, win rate , pnl, and wallet balance