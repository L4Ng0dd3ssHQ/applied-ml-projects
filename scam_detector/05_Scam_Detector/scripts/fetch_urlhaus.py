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

if response.status_code == 200:
    save_path = "../data/raw/urlhaus_full.csv.zip"
    with open(save_path, "wb") as f:
        f.write(response.content)
    print(f"File saved to {save_path}")
else:
    print(f"Failed - status code: {response.status_code}")