import requests
from datetime import datetime
from decouple import config

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = config('USER_NAME')
TOKEN = config("TOKEN")
GRAPH_ID = "graph1"
print(USERNAME, TOKEN)
# 1. creating the user account
user_params ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text) # response is subsequently "user already exist"

# 2. Create the graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding daily",
    "unit": "day",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Update graph i.e. set the unit from days to hours and color
graph_update_config = {
    "unit": "hours",
    "color": "momiji"
}
graph_update_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
# response = requests.put(url=graph_update_endpoint, json=graph_update_config, headers=headers)
# print(response.text)


# 3. Add pixel data
# today = datetime(year=2022, month=12, day=19)
today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_creation_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? ")
}
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_config, headers=headers)
print(response.text)

# 4. Update yesterdays value
update_pixel_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"
update_pixel_config = {
    "quantity": "8"
}
# response = requests.put (url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# 5. Delete a pixel
# use the updated date
# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)

