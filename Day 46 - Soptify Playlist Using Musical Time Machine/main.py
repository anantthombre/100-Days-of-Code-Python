from bs4 import BeautifulSoup
import requests

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