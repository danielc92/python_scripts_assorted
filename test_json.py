import pandas as pd

#TRANSFORMING LIST OF DICTIONARIES INTO DATA FRAME

dict_list = [
    {
		"COLOUR": "red",
		"VALUE": "#f00"
	},
	{
		"COLOUR": "green",
		"VALUE": "#0f0"
	},
	{
		"COLOUR": "blue",
		"VALUE": "#00f"
	},
	{
		"COLOUR": "cyan",
		"VALUE": "#0ff"
	},
	{
		"COLOUR": "magenta",
		"VALUE": "#f0f"
	},
	{
		"COLOUR": "yellow",
		"VALUE": "#ff0"
	},
	{
		"COLOUR": "black",
		"VALUE": "#000"
	}]

#1. create list containing key names

key_names = []
for key in dict_list[0].keys():
    key_names.append(key)
print(key_names)

#2. create var storing number of dictionaries in list

num_keys = len(dict_list[0].keys())
num_dicts = len(dict_list)

#3. create new dictionary to store the nested dictionaries in
new_dict = {}

for n in range(num_keys):
    new_dict[key_names[n]] = []

#4. nested for loop assigns each value from nested dictionary to new dictionary
for dict in dict_list:
    for key_number in range(num_keys):
        new_dict[key_names[key_number]].append(dict[key_names[key_number]])

my_data = pd.DataFrame(new_dict)

my_data.rename(columns = {"COLOUR":"Colour","VALUE":"Value"}, inplace = True)

print(my_data)


################################################################################



nested_crap = {
    "name":"John",
    "age":30,
    "cars": {
        "car1":"Ford",
        "car2":"BMW",
        "car3":"Fiat"
    }
}

print(type(nested_crap["name"]))

print(nested_crap["name"])

print(type(nested_crap["age"]))

print(nested_crap["age"])

print(type(nested_crap["cars"]))

print(nested_crap["cars"])