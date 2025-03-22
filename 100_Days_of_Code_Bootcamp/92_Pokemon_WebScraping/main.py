from bs4 import BeautifulSoup
import requests

# https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_Kanto_Pok%C3%A9dex_number
# access in 18/02/2022

with open("pokemon_encyclopedia.html", encoding="utf8") as file:
    soup = BeautifulSoup(file, "html.parser")
    print(soup.prettify())
