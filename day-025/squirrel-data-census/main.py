# Day 025
import pandas
COL_FUR_COLOR = "Primary Fur Color"
data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
# get the unique fur colors
fur_colors = data[COL_FUR_COLOR].unique()
grey_squirrels_count = len(data[data[COL_FUR_COLOR] == "Grey"])
red_squirrels_count = len(data[data[COL_FUR_COLOR] == "Cinnamon"])
black_squirrels_count = len(data[data[COL_FUR_COLOR] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)


# create dataframe
squirrel_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
squirrel_data_frame = pandas.DataFrame(squirrel_dict)
print(squirrel_data_frame)
squirrel_data_frame.to_csv("squirrel_count.csv")
