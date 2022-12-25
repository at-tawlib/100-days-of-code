from bs4 import BeautifulSoup
import requests

# get data from a live site [ycombinator.com]
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)

# get title of first article
article_title = soup.find("span", class_="titleline")
print(article_title)
article_text = article_title.getText()
print(article_text)
article_link = article_title.find("a")
print(article_link.get("href"))
article_score = soup.find("span", class_="score")
print(article_score.getText())


articles = soup.find_all("span", class_="titleline")
articles_texts = []
articles_links = []
for article in articles:
    text = article.getText()
    articles_texts.append(text)
    link = article.find("a").get("href")
    articles_links.append(link)

# get upvotes, trim to get only number, convert it to int
articles_upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

print(articles_texts)
print(articles_links)
print(articles_upvotes)

# print out the title and link for the story with the highest number of upvotes.
# use index of the largest number inside the article_upvotes
largest_number = max(articles_upvotes)
largest_index = articles_upvotes.index(largest_number)

print(articles_texts[largest_index])
print(articles_links[largest_index])
print(articles_upvotes[largest_index])
