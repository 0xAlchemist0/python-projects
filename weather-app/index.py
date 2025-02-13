import requests
import json
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv()



#how to make a object in pyton
body = {
 "Content-Type": "application/json"
}

endpoints =  {
     "current": "/current.json",
     "forecast": "/forecast.json",
     "autocomplete": "/search.json",
     "history":"/history.json"
}

def findTargetWeather():
  user_input = input("what type of weather do you want? (forecast or current weather): ")
  target_endpoint = findTypeKey(user_input)
  location_input = input("Enter the location you would like to check the location of: ")
  time_input = input("Enter how many days you want to check the weather?: ")
  API_URL = build_request_URL(target_endpoint, location_input, time_input)
  data_obtained = makeRequest(API_URL, body)
  output = dissect_data(data_obtained, "current")
  
def findTypeKey(type):
     target = ""
     #how to loop through a single object in python
     #why the fuck is it a brainfuck to deal with json lmao 
     for key,value in endpoints.items():
          #to find if a string is contained in another string yopu do variable1 in variable2
          if(str(key) in type): 
            print(f"found : {key}")
            target = value
           
               
     return target

#left off here dissecting data to find right values possibly end up returning a tuple (value1, value2)
def dissect_data(response, key):
      for key, value in response.items():
          if (key == "current"):
               weather_data = value
               print(weather_data)
               for key,value in weather_data.items():
                     print(key)
          
          

def build_request_URL(endpoint, location, time):
     #create the right url to make the proper request
     base_url = "http://api.weatherapi.com/v1/"
     return base_url + endpoint + f"?key={os.getenv("API_KEY")}&q={location.lower()}&days=${time}"

def makeRequest(URL, body):
     #how to call a api and apass in the body you must include body= or headers so it detects it as header or body
     #body is a variable scroll up
     output = ""
     resposne = requests.post(URL, headers=body)
     #when we get the response we have to use .json to get the json response
     if (resposne.status_code == 200): output = resposne.json()
     else: output = "Error invalid API call"
     return output
        
findTargetWeather()



