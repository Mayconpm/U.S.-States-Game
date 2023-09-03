import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# TODO: squirrel_count.csv fur_colar an count


fur_color = squirrel_data.groupby(["Primary Fur Color"], group_keys=False)["Unique Squirrel ID"].count().reset_index()
fur_color.rename(columns={"Primary Fur Color": "Fur_Color", "Unique Squirrel ID": "Count"}, inplace=True)
fur_color.to_csv("fur_color.csv")
