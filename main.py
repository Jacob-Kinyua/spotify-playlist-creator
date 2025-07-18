from bs4 import BeautifulSoup
import requests
import time

BROSWER_URL = "https://www.billboard.com/charts/hot-100/"

date_preference = input("Which year do you want to travel to?Input in the format YYYY-MM-DD: ")

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

time.sleep(2)
response = requests.get(url=f"{BROSWER_URL}{date_preference}/", headers=headers)
content = response.text

soup = BeautifulSoup(content, "html.parser")

titles_lst = []

div = soup.find("div", class_="chart-results-list")
titles = div.find_all("h3", id="title-of-a-story")
for title in titles:
    if title.get_text(strip=True) not in ["Gains in Weekly Performance", "Additional Awards", "Songwriter(s):", "Producer(s):", "Imprint/Promotion Label:"]:
        song = title.getText(strip=True)
        titles_lst.append(song)

print(titles_lst)
print(len(titles_lst))