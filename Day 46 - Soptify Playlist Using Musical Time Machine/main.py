from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Enter the date in this format YYYY-MM-DD: ")

URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(URL)

songs_webpage = response.text

soup = BeautifulSoup(songs_webpage, "html.parser")

# print(soup.title)

# all_songs = soup.find_all(name="li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max")
# print(all_songs)

# songs_title = [song.getText() for song in all_songs]

# print(songs_title)

songs_title = soup.find_all("h3", class_="a-no-trucate", id="title-of-a-story")

songs_list = [song.getText().strip() for song in songs_title]

# songs_list = []

# for song in songs_title:
#     songs_list.append(song.get_text().strip())

print(songs_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-public",
        redirect_uri="http://example.com",
        client_id="Client ID",
        client_secret="Client Secret ID",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
# print(user_id)

# song_uris = []
# year = date.split("-")[0]
# for song in songs_list:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")


#Creating a new private playlist in Spotify
# playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=True)
# print(playlist)

#Adding songs found into the new playlist
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


# Create a Spotify Playlist and get the Playlist ID
playlist = sp.user_playlist_create(
    user=user_id,
    name=f'Hot 100: {date}',
    public=False,
    # collaborative=False,
    description='Hot 100 from billboard.com'
)

# print(response)  # Print the response to examine the structure
playlist_id = playlist["id"]  # This is used when you add tracks to the playlist

# Search Spotify for tracks and add the URI to list
song_uris = []
for song in songs_list:
    song_details = sp.search(
        q=f"track:{song}",  # year:{year}",
        limit=1,
        type="track",
        market="GB",  # market="from_token",
    )
    try:
        song_uri = song_details["tracks"]["items"][0]["uri"]
        # print(song_uri)
        song_uris.append(song_uri)
    except IndexError:
        print(f"{song} doesn't exist on Spotify.")

    
    # Add tracks to Spotify Playlist
sp.playlist_add_items(
    playlist_id=playlist_id,
    items=song_uris,
    position=None
)