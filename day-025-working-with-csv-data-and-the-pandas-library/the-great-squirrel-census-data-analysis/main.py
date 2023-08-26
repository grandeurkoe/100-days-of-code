import pandas

gray_squirrel_counter = 0
cinnamon_squirrel_counter = 0
black_squirrel_counter = 0

squirrel_dataset = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_color_data = squirrel_dataset["Primary Fur Color"]

for each_color in range(squirrel_color_data.size):
    if squirrel_color_data[each_color] == "Gray":
        gray_squirrel_counter += 1
    elif squirrel_color_data[each_color] == "Cinnamon":
        cinnamon_squirrel_counter += 1
    elif squirrel_color_data[each_color] == "Black":
        black_squirrel_counter += 1

squirrel_color_count = {
    "Squirrel Fur Color": ["Gray", "Cinnamon", "Black"],
    "Squirrel Count": [gray_squirrel_counter, cinnamon_squirrel_counter, black_squirrel_counter],
}

data = pandas.DataFrame(squirrel_color_count)
data.to_csv("squirrel_color_count.csv")
