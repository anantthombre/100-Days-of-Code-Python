#import requests
#from bs4 import BeautifulSoup
from requests_html import HTMLSession

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
session = HTMLSession()
webpage = session.get(URL)

webpage.html.render()
all_movies = webpage.html.find(selector="h3")

movie_titles = [movie.text for movie in all_movies]
#print(movie_titles)

movies = movie_titles[::-1]

# for movie in movies:
#     print(movie)
    
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")