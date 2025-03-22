import requests
import smtplib


def send_email(messsage: str):
    my_email = ""
    my_password = ""

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg=f"Subject:Weather conditions\n\n{messsage}")
        connection.close()
        print("Email sent")


OPEN_WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = ""
MY_LAT = -16.020901
MY_LONG = -48.067291
EXCLUDE = ""

parameters = {"lat": MY_LAT, "lon": MY_LONG, "appid": API_KEY, "exclude": EXCLUDE}

response = requests.get(url=OPEN_WEATHER_ENDPOINT, params=parameters)
print(response.status_code)
response.raise_for_status()
data = response.json()
hourly_data = data["hourly"]

bring_umbrella = False
for n in range(0, 12):
    weather_code = hourly_data[n]["weather"][0]["id"]
    print(weather_code)
    if weather_code < 700:
        bring_umbrella = True

if bring_umbrella:
    send_email("You will need an Umbrella in next 12 hours")
else:
    send_email("You will not need an Umbrella in next 12 hours")
