import requests
from datetime import datetime


USERNAME = ""
TOKEN = ""
GRAPH_ID = ""
pixela_endpoint = "https://pixe.la/v1/users"
today = datetime.now()

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

post_pixel = {
    # "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.put(url=post_pixel_endpoint, json=post_pixel, headers=headers)
print(response.text)
