#This code no longer work because sites changed the
#HTML used to render the pages


from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512/")
soup = BeautifulSoup(response.text, "html.parser")
data = (soup.find())
print(data)


#
# with open("index.html") as file:
#     soup = BeautifulSoup(file.read(), "html.parser")
#
# tags = soup.find_all(name="a")
#
# for tag in tags:
#     print(tag.getText())
