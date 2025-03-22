from bs4 import BeautifulSoup
import requests

target_price = int(input("What is the target price?\n"))

# response = requests.get("URL for the product")
# soup = BeautifulSoup(response.text, "html.parser")
# current_price(soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString"))

current_price = "R$ 2650,00"

prov = current_price.replace("R$ ", "")
current_price = prov.replace(",", "")
current_price = (int(current_price))/100

if current_price < target_price:
    print("It's time to buy")
    # send email()
else:
    print("It's not the time to buy")

print(f"Your target price is {target_price}")
print(f"Today the price is {current_price}")

# amazon blocked the conection
# possible workarounds
# 1 download the page and save to file
# 2 supose we got back the string "R$ 2650,00"
# work with the amazon API