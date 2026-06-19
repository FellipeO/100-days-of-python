import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_list = data["Primary Fur Color"].to_list()
count_dict = {}
for item in color_list:
    if item not in count_dict:
        count_dict[str(item)] = 0
    else:
        count_dict[str(item)] += 1

del count_dict["nan"]

df = pd.DataFrame(list(count_dict.items()), columns=["Fur Color", "Count"])

df.to_csv("squirrel_count")




