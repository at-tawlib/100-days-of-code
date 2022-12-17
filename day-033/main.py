import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)
# # de;ete a letter from the website to raise an error
# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")
response.raise_for_status()
# get data
data = response.json()
print(data)

data1 = response.json()["iss_position"]
print(data1)

data2 = response.json()["iss_position"]["longitude"]
print(data2)

longitude = data["iss_position"]["longitude"]
print(longitude)

latitude = data["iss_position"]["latitude"]
print(latitude)

iss_position = (longitude, latitude)
print(iss_position)