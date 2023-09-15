import requests
from bs4 import BeautifulSoup

reversed_top_100 = []
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Fetch top 100 movies data from the above URL.
empire_response = requests.get(url=URL)
empire_response.raise_for_status()
empire_contents = empire_response.text

# Use BeautifulSoup parser to parse through the content that you received from the website.
empire_soup = BeautifulSoup(empire_contents, "html.parser")
empire_top_100 = empire_soup.select(selector=".listicleItem_listicle-item__title__hW_Kn")

for each_movie in empire_top_100:
    reversed_top_100.append(each_movie.get_text())

top_100 = reversed_top_100[::-1]

# Write the top 100 movies to "movies.txt".
with open(file="movies.txt", mode="w", encoding="utf8") as movie_connect:
    for movie in top_100:
        movie_connect.write(f"{movie}\n")
