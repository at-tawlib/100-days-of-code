import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}
# get 10 questions from the api
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]