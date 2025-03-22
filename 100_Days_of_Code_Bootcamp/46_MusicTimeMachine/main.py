from bs4 import BeautifulSoup
import requests

year = 2007
month = 6
day = 23

response = requests.get("https://www.billboard.com/charts/hot-100/2012-08-12")
soup = BeautifulSoup(response.text, "html.parser")
names = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

for name in names:
    print(name.text)
