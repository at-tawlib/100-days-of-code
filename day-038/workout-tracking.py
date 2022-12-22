import requests
from datetime import datetime
from decouple import config

APP_ID = config('APP_ID')
APP_KEY = config('APP_KEY')
END_POINT = config('END_POINT')
SHEET_ENDPOINT = config('SHEET_ENDPOINT')
SHEET_API = config('SHEET_API')
BEARER_TOKEN = config('BEARER_TOKEN')

GENDER = "male"
WEIGHT = 70.0
HEIGHT = 172.4
AGE = 32

exercise_text = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key":APP_KEY
}

request_body = {
 "query": exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT,
 "height_cm": HEIGHT,
 "age": AGE
}
# Post an exercise
response = requests.post(url=END_POINT, json=request_body, headers=headers)
result = response.json()
print(response.text)
print(result)

# insert answer in Sheet row
# today = datetime.today()
# today_string = str(today.strftime("%d/%m/%Y %H:%M:%-S"))
# date, time = today_string.split(" ", 1)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

headers = {
    "Authorization" : BEARER_TOKEN
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, headers=headers)
    print(sheet_response.text)