#     #### Working with data files: CSV files with Pandas libraries
#
# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# # data = pandas.read_csv("weather_data.csv")
# # #print(type(data))
# # #print(type(data["temp"]))
# #
# # # data_dict = data.to_dict()
# # # print(data_dict)
# # temp_list = data["temp"].to_list()
# # # print(temp_list)
# # # average = sum(temp_list) / len(temp_list)
# # # print(average)
# # #or
# # #print(data["temp"].mean())
# # #print(data["temp"].max())
# # #print(data.temp.max())
# #
# # # How to get data in the row of my dataframe
# #
# # #print(data[data.day == "Monday"])
# # #print(data[data.temp == data.temp.max()])
# #
# # monday = data[data.day == "Monday"]
# # #print(monday.condition)
# # monday_temp = int(monday.temp)
# # monday_temp_F = monday_temp * 9/5 + 32
# # print(monday_temp_F)
#
# #Create a data frame from scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")

import pandas
squirrel_data = pandas.read_csv("2018CPS_Squirrel_Data.csv")
gray_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
red_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

squirrel_dict = {
"Fur Color": ["Gray", "Red", "Black"],
"Count": [gray_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(squirrel_dict)
df.to_csv("squirrel_count.csv")




