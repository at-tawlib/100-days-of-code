# day-025 09-12-2022

import csv

with open("./weather-data.csv") as csv_file:
    # get data from the .csv file
    data = csv.reader(csv_file)
    print(data)
    temperatures = []
    for row in data:
        print(row)
        # extract temperature into a list
        if row[1] != "temp":
            temperatures.append(row[1])
    print(temperatures)     # print temperature list

