import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from decouple import  config

SPOTIPY_CLIENT_ID = config("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET_ID = config("SPOTIPY_CLIENT_SECRET_ID")
SPOTIPY_REDIRECT_URI = "http://example.com"

# SCRAPING BILLBOARD TOP 100
# ask user year to get song from billboard top 100
song_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# get top 100 songs from the site on the specified date
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{song_date}")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
songs = soup.select(selector="li ul li h3")
song_names = [song.getText().strip() for song in songs]

# spotify authentication and get token (includes user id) into token.txt
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET_ID,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_ID = sp.current_user()["id"]

# create uris of songs to add to the playlist
song_uris = []
song_year = song_date.split("-")[0]
songs_skipped = 0
for song in song_names:
    # search for song in spotify by title and year
    result = sp.search(q=f"track:{song} year:{song_year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exit in Spotify. Skipped.")
        songs_skipped += 1

# create private playlist with name "YYYY-MM-DD Billboard 100"
playlist = sp.user_playlist_create(user=user_ID, name=f"{song_year} Billboard 100", public="False")

# add songs to playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"{len(song_uris)} songs added and {songs_skipped} skipped")