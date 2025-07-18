import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests
import time
from dotenv import load_dotenv
import os
import pprint

load_dotenv()

# creates spotify token
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri=os.getenv("REDIRECT_URL"),
    scope="playlist-modify-private"
))

user = sp.current_user()
user_id = user["id"]


pp = pprint.PrettyPrinter(indent=4)



BROSWER_URL = "https://www.billboard.com/charts/hot-100/"

date_preference = input("Which year do you want to travel to?Input in the format YYYY-MM-DD: ")

# creayes new playlist
playlist_name = f"{date_preference[:4]} Top 100 Playlist"
playlist_description = "Created with Spotipy"
new_playlist = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    description=playlist_description
)

playlist_id = new_playlist["id"]

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

time.sleep(2)
response = requests.get(url=f"{BROSWER_URL}{date_preference}/", headers=headers)
content = response.text

soup = BeautifulSoup(content, "html.parser")

titles_lst = []

# adds top 100 tracks of a certain year to the new playlist
div = soup.find("div", class_="chart-results-list")
titles = div.find_all("h3", id="title-of-a-story")
for title in titles:
    if title.get_text(strip=True) not in ["Gains in Weekly Performance", "Additional Awards", "Songwriter(s):", "Producer(s):", "Imprint/Promotion Label:"]:
        song = title.getText(strip=True)
        titles_lst.append(song)
        track= song
        year= int(date_preference[:4])
        query= f"track:{track} year:{year}"
        try:
            results = sp.search(q=query, type="track", limit=1)
            track_uris = [track["uri"] for track in results["tracks"]["items"]]
            sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)
            print("Added track to playlist:", new_playlist["external_urls"]["spotify"])
        except:
            print('File Not Found')
