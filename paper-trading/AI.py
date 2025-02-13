from dotenv import load_dotenv
import os
from google import genai
load_dotenv()

gemini = os.getenv("GEMINI_KEY")
#try except is basically a try catch block
def providePrompt(prompt):
    try:
        client  = genai.Client(api_key=gemini)
        response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"{prompt}")
        print(response.text)
    
    #we name the error which is stored in Exception as error to rpint it
    except Exception as error:
     print(error)
     
    return None