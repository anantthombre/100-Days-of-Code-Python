from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
#print(soup.title)

all_articles = soup.find_all(name="span", class_="titleline")

article_text = []
article_link = []

for article in all_articles:
    article_text.append(article.find("a").getText())
    article_link.append(article.find("a").get("href"))


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_text)
# print(article_link)
# print(article_upvotes)

max_upvote_index = article_upvotes.index(max(article_upvotes)) # Index of highest upvote


print(article_text[max_upvote_index])
print(article_link[max_upvote_index])
print(article_upvotes[max_upvote_index])


