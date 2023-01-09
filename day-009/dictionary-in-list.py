travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

    # dict_travel = {
    #     "country": country,
    #     "visits": visits,
    #     "cities": cities
    # }
    # travel_log.append(dict_travel)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)