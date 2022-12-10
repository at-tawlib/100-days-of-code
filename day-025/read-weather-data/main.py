# day-025 09-12-2022

# import csv
#
# with open("./weather-data.csv") as csv_file:
#     # get data from the .csv file
#     data = csv.reader(csv_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         print(row)
#         # extract temperature into a list
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)     # print temperature list

import pandas

data = pandas.read_csv("weather-data.csv")
# print(data)
# print(data["temp"])

# get data into a dictionary
data_dict = data.to_dict()
print(f"dictionary: {data_dict}")

# get data into list
temp_list = data["temp"].to_list()
print(f"temperature list: {temp_list}")

# calculate the average temperature
average_temp = sum(temp_list) / len(temp_list)
print(f"average temperature = {average_temp}")

# use pandas to get mean (average), max, min
print(f'mean: {data["temp"].mean()}')
print(f'max: {data["temp"].max()}')
print(f'min: {data.temp.min()}')

# get data with the column name directly
print(data.temp)
print(data.condition)

# get data in row / filtering data by column
# get row data if data.day == monday
print(data[data.day == "Monday"])

# print row with the highest temperature
print(data[data.temp == data.temp.max()])

# get Monday's condition
monday = data[data.day == "Monday"]
print(monday.condition)

# convert Monday's temperature to Fahrenheit
# (celsius_value * 9/5) + 32
celsius_value = int(data[data.day == "Monday"].temp)
fahrenheit_value = (celsius_value * 9/5) + 32
print(f"Celsius = {celsius_value}, Fahrenheit = {fahrenheit_value}")





















