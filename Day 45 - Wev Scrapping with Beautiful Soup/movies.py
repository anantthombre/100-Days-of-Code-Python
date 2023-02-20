import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

#print(soup.prettify)
print(soup.title)

# all_movies = soup.select("h3.jsx-4245974604")
#find(name="h3", class_="jsx-4245974604")

# print(all_movies)

#movie_title = [movie.getText() for movie in all_movies]


#movies = movie_title[::-1]
#print(movies)
