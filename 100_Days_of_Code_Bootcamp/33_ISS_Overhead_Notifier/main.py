import requests
from datetime import datetime
import smtplib


def send_email():
    my_email = ""
    my_password = ""

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg=f"Subject:Space Station Reminder\n\nThe space station is in range")
        connection.close()
        print("Email sent")


def check_position():
    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5) < iss_latitude < (MY_LAT + 5):
        if (MY_LONG - 5) < iss_longitude < (MY_LONG + 5):
            return True
        else:
            return False
    else:
        return False


# Your latitude
MY_LAT = -16.020901
# Your longitude
MY_LONG = -48.067291

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

print(f"latitude: {iss_latitude} longitude: {iss_longitude}")

if check_position():
    print("Space station in range")
    time_in_hours = int(time_now.time().hour)

    if 18 <= time_in_hours <= 6:
        send_email()
else:
    print("Space station is not in range")
