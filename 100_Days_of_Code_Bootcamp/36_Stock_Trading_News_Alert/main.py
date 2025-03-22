import requests
import datetime
import smtplib
import html


def send_email(message: str):
    my_email = ""
    my_password = ""

    with smtplib.SMTP("smtp.gmail.com") as connection:
        unescaped_message = html.unescape(message)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg=f"Subject:Finance Report\n\n{unescaped_message}")
        connection.close()
        print("Email sent")

final_message = ""
API_ENDPOINT = "https://www.alphavantage.co/query"
STOCK = "GOOGL"
API_KEY = ""


def get_today_date_formated(days_before: int):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=days_before)
    return str(yesterday)


params_dict = {"function": "TIME_SERIES_DAILY", "symbol": STOCK, "apikey": API_KEY}
response = requests.get(url=API_ENDPOINT, params=params_dict)
response.raise_for_status()
stock_data = response.json()

final_message += f"{STOCK} stocks\n"
final_message += (f"Last 7 days report\n")

n = 1
counter = 1
while n < 8:
    try:
        str_a = ("date: " + get_today_date_formated(counter))
        str_b = f"\nOpen price: {stock_data['Time Series (Daily)'][get_today_date_formated(counter)]['1. open']}$ Dollars\n\n"
    except KeyError:
        pass
        # final_message += ("No data registered in: " + get_today_date_formated(counter) + "\n")
    else:
        final_message += str_a
        final_message += str_b
        n += 1
    finally:
        counter += 1


NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ""
news_params_dict = {"q": "Google", "from": "2021-09-10", "sortBy": "popularity", "apikey": NEWS_API_KEY}

response = requests.get(url=NEWS_API_ENDPOINT, params=news_params_dict)
articles = response.json()["articles"]
three_articles = articles[:3]
final_message +=("\nLast relevant news related to this company:\n")
for article in three_articles:
    final_message +=("\n")
    final_message += article["title"].encode('ascii', 'ignore').decode('ascii')
    final_message += article["description"].encode('ascii', 'ignore').decode('ascii')
    final_message +=("\n")

send_email(final_message)
