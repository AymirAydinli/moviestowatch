import requests
from bs4 import BeautifulSoup
import os

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")

movie_titles_h3 = soup.find_all(name='h3', class_='title')


movie_titles = [title.getText() for title in movie_titles_h3]
print(movie_titles)

for title in movie_titles[::-1]:
    with open('movies.txt', 'a') as file:
        file.write(title + '\n')