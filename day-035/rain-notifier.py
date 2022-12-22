import requests

# I did not use the One API call for this project because of the subscription
# lat and long for Accra
API_KEY = "eb4582808b8b412bac02cb6b48444624"
LATITUDE = 5.603717
LONGITUDE = -0.186964
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
# weather data for five days with call for every 3 hours
OWM_Endpoint_Five_Day = "https://api.openweathermap.org/data/2.5/forecast"
OWM_Endpoint_One_Call = "https://api.openweathermap.org/data/3.0/onecall"
parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY
}

response = requests.get(url=OWM_Endpoint_Five_Day, params=parameters)
response.raise_for_status()
data = response.json()
# get list for the next 12 hours [4 items since data is every 3 hours]
first_twelve_hours = data['list'][:4]

will_rain = False
# check if any of the condition is < 700 (raining) and send message to bring umbrella
for hour_data in first_twelve_hours:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 900:
        will_rain = True

if will_rain:
    print("Bring an umbrella")

# run everyday at 7 am to check whether it will rain that day

