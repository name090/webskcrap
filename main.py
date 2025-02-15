import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

data = dict()


for i in range(len(quotes)):
    data[quotes[i].text] = authors[i].text

with open("quotes.text", "w", encoding="utf-8") as file:
    data = str(data)
    file.write(data)