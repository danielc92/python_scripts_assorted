import pandas as pd
import numpy as np

l1 = [1,2,3,4,5,6]
l2 = ["a","d","d","ea","d","ef"]
l3 = [True,True,False,True,True,False]
l4 = [45,15,35,15,18,0]

ser_l1 = pd.Series(l1)
ser_l2 = pd.Series(l2)

df = pd.concat([ser_l1, ser_l2], axis = 1, keys = ['num','let'])


s = df['num']

s_list = s.tolist()

big_list = [l1,l2,l3,l4]

print("Original Dataframe: " + str(df))
'''
print(ser_l2)

print(ser_l1)

print(s)

print(s_list)

print(big_list)

print(df[(df["let"] == "d") | (df["let"] == "ef")])

print(df[[df["num"] > 3]])
'''
print("\n\n")



test = df[df["num"] != 2]
print("test " +str(test))

print(test.iloc[1])
#print(test.loc[1])

print(df.replace(["d",2,3],["WOOOOOD",32,20]))

for col in df.columns:
    print(col)
    print
