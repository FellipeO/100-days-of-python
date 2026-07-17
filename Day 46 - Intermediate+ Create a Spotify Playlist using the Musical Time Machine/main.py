import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

BASE_URL = "https://appbrewery.github.io/bakeboard-hot-100/"
header = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:152.0) Gecko/20100101 Firefox/152.0"}
#travel_year = input("Which year would you like to travel to? Type the date in a YYYY-MM-DD format: ")
travel_year = "2004-07-24"
response = requests.get(f"{BASE_URL}/{travel_year}", headers=header)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

song_list = [song.text for song in soup.find_all(name="h3", class_="chart-entry__title")]
artist_list = [artist.text for artist in soup.find_all(name="span", class_="chart-entry__artist")]

yt = YTMusic("browser.json")
playlists = yt.get_library_playlists()
playlist_exists = False
video_ids = []
for playlist in playlists:
    if playlist["title"] == f"{travel_year} Billboard 100":
        playlist_exists = True
if not playlist_exists:
    billboard_id = yt.create_playlist(f"{travel_year} Billboard 100", f"Top 100 songs as of {travel_year}", "PRIVATE")
    for i in range(0, len(song_list)):
        results = yt.search(f"{artist_list[i]} {song_list[i]}", filter="songs")
        try:
            print(f"Adding {results[0]["title"]}")
        except IndexError:
            print("Song Not Found!")
        video_ids.append(results[0]["videoId"])
    yt.add_playlist_items(billboard_id, video_ids)
