# with open(file="weather_data.csv", mode="r") as read_weather_data:
#     data = read_weather_data.readlines()
#
# for data_point in range(len(data)):
#     data[data_point] = data[data_point].strip()
#
# print(data)

# OR

# import csv
#
# with open(file="weather_data.csv", mode="r") as read_weather_data:
#     # The reader() function creates a csv object.
#     data = csv.reader(read_weather_data)
#     temperature = []
#     # This 'data' csv object can be looped through to get individual row data.
#     for row in data:
#         if row != ['day', 'temp', 'condition']:
#             temperature.append(int(row[1]))
#         print(row)
#
# print(temperature)

# OR

import pandas

data = pandas.read_csv(filepath_or_buffer="weather_data.csv")
# Convert data to dictionary.
data_dict = data.to_dict()

# temp_list = data["temp"].tolist()
# average_temp = sum(temp_list)/ len(temp_list)
# print(average_temp)

# OR

# average_temp = data["temp"].mean()
# print(f"Average Temperature : {average_temp}")
#
# max_temp = data["temp"].max()
# print(f"Maximum Temperature : {max_temp}")

# Get Data in Columns.

# print(data["condition"])
# OR
# print(data.condition)

# Get Data in Row.
# print(data[data.day == "Monday"])
# print(data[data.temp == max_temp])

# monday_data = data[data.day == "Monday"]
# monday_ctof = (int(monday_data.temp) * 9/5) + 32
# print(monday_ctof)

# Create Dataframe from Scratch.

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 64, 52]
}

data = pandas.DataFrame(data_dict)
data.to_csv("student_data.csv")

