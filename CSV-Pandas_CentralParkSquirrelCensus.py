import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(data)

grey_counter = (data['Primary Fur Color']=='Gray').sum()
red_counter = (data['Primary Fur Color']=='Cinnamon').sum()
black_counter = (data['Primary Fur Color']=='Black').sum()

squirrel_dict = {
    'Fur Color': ["grey", "red", "black"],
    'Count': [grey_counter, (data['Primary Fur Color']=='Cinnamon').sum(), black_counter]
}
print(squirrel_dict)
squirrel_count = pandas.DataFrame(squirrel_dict)
squirrel_count.to_csv("squirrel_count.csv")
