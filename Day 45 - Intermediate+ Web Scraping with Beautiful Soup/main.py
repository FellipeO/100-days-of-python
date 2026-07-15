import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073(855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
names = soup.find_all(name="h3", class_="title")
ordered_names = []
for i in range(len(names)-1, -1, -1):
    ordered_names.append(names[i].text)

with open("movies.txt", "w") as file:
    for name in ordered_names:
        file.write(f"{name}\n")
