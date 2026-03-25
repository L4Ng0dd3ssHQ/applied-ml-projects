#import libraries
import requests
import os
from dotenv import load_dotenv

#load env
load_dotenv()
URLHAUS_KEY = os.getenv("URLHAUS_KEY")

url = f"https://urlhaus-api.abuse.ch/v2/files/exports/{URLHAUS_KEY}/full.csv.zip"

#send request
response = requests.get(url)
#status check
if response.status_code == 200:
    print("Download successful")
else:
    print(f"Failed - status code: {response.status_code}")
    