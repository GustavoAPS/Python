import requests
import os

APPLICATION_ID = "e3c499f3"
API_KEY = "719af4b8726d4412b63c0adad45a4aa5"

ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": API_KEY
}

params = {
    "query": "ran 3 miles",
    "gender": "female",
    "weight_kg": "72.5",
    "height_cm": "167.64",
    "age": "30"
}

add_row = "https://api.sheety.co/74ec95c554661f91c0dfa772b3c0cf54/myWorkouts/workouts"
retrieve_rows = "https://api.sheety.co/74ec95c554661f91c0dfa772b3c0cf54/myWorkouts/workouts"

exercise_params = {
    "workout": {
        "date": "13/09/2021",
        "time": "22:21",
        "exercise": "Run",
        "duration": "30:00",
        "calories": "100"
    }
}

# response = requests.post(url=ENDPOINT, json=params, headers=headers)
response = requests.post(url=retrieve_rows, json=exercise_params)
print(response.status_code)
print(response.json())
