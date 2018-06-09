def p(p):
    print(str(p) + "\n")

import pandas as pd
import numpy as np

my_dict = {"age": [10,12,15,14,15,16], "name":['jan','rufus','susan','rupert','gary','david'], "score":[50 ,85,70,65,80,87] }

samp = pd.DataFrame(my_dict, columns = ["name","age","score"])

my_dict2 = {"name": ['jan','rufus','susan','rupert','gary','david'], "height":[124,140,115,110,122,120] , "weight":[25,35,27,25,20,19]}

u = []
for i in my_dict2.keys():
    u.append(i.upper())

samp2 = pd.DataFrame(my_dict2)

samp2.rename(columns = {"name" : "FULL NAME"}, inplace= True)

p("Creating DataFrame.")
p(samp2)


'''
# samp.rename(columns={"name":"Full Name"}, inplace = True)
#     #,"age":"Student Age","score":"Student Score"})
# p("Replace column names.")
# p(samp)


samp.replace([80, 90], [82,99], inplace = True)
p("Replacing values in all columns.")
p(samp)


# samp.replace('(^\s+|\s+$)','', regex = True, inplace = True) #Front AND end spaces
# p("Replacing all spaces on left and right all cells")
# p(samp)


p("Join samp1 and samp2 based on 'name' column")
samp3 = samp.merge(samp2, on = "name", how = "inner")
p(samp3)


p("Deleting the 'height' column from samp3")
samp3.drop(columns = 'height', inplace = True)
p(samp3)


p("Deleting row with index 0 and 1 from samp3")
samp3.drop([0,1], inplace = True)
p(samp3)

p(samp.describe())
p(samp.mean())
p(samp.mean())
p(samp.count())

p(samp.dtypes)
samp.name = samp.name.astype(str, inplace = True)
p(samp.dtypes)


#generate 6 row by 4 column test data
td1 = round(pd.DataFrame(np.random.rand(6,4)),3)
p(td1)

td2 = round(pd.DataFrame(np.random.rand(6,2)),3)
p(td2)

td3 = round(pd.DataFrame(np.random.rand(2,4)),3)
p(td3)

#add dataframes vertically (Rows)
p(td1.append(td2))

p(pd.concat([td1,td2],axis = 1))


#ADDING SERIES TO DATAFRAME

dict = {
    "        David":[1,2,4]
    ,"      Susan       ":[4,3,15]
    ,"Leo":[455,333,243]
    ,"Jerry":[33,21,12]
}


data = pd.DataFrame(dict)

for col in data.columns:
    data.rename(columns = {col:col.strip().upper()}, inplace = True)

print(str(data) + "\n")

data.to_csv("data.csv", index_label = "ROW_INDEX")

ser1 = pd.Series(data["SUSAN"] * 2.125664, name = "CLOCK")
print(ser1)

data2 = pd.concat([data, ser1], axis = 1)
print(data2)

#POPULATING NULLS WITH COLUMN AVERAGES

d = {
    0:[1,2,3,4],
    1:[1,2,3,4],
    2:[1,2,None,None],
    3:[None,2,3,4]
}

data = pd.DataFrame(d)
data.rename(columns = {0:"BANANA",1:"APPLE",2:"ORANGE",3:"PEANUT"}, inplace = True)


data_no_more_nulls = data.fillna(data.mean())

print(data_no_more_nulls)


#remove duplicates

dict = {
        "pid":  ["p001","p001","p002","p003","p003","p004"],
        "sale": [5,5,15,4,15,15],
        "unit": [2,2,6,8,16,6],
       }

data = pd.DataFrame(dict)

print(data)

row_count = data.shape[0]

row_dictionary = {
                    0 : [],
                    1 : [],
                    2: [],
                    3: [],
                    4: [],
                    5: []
                  }

string_dictionary = {}

for row_number in range(row_count):
    for col in data.columns:
        row_dictionary[row_number].append(data.loc[row_number, col])

print(row_dictionary)

mega_list = []
bad_row_ids = []

for k in row_dictionary.keys():
    
    if row_dictionary[k] not in mega_list:
        mega_list.append(row_dictionary[k])

    else:
        bad_row_ids.append(k)

print(bad_row_ids)
print(mega_list)
'''