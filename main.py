from bs4 import BeautifulSoup
import requests
import time

BROSWER_URL = "https://www.billboard.com/charts"

date_preference = input("Which year do you want to travel to?INput in the format YYYY-MM-DD: ")

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

time.sleep(5)
response = requests.get(url=f"{BROSWER_URL}/date_preference", headers=headers)
content = response.text


