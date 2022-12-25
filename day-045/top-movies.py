from bs4 import BeautifulSoup
import requests

# get data from website
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
web_data = response.text

soup = BeautifulSoup(web_data, "html.parser")
# get all titles of movies
movie_titles = soup.find_all(name="h3", class_="title")
movie_titles.reverse()
movies = [movie.text for movie in movie_titles]
# save movies in txt file
with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
