import pandas as pd
import numpy as np
import datetime as dt


data = pd.read_excel("datasets\\test_melt.xlsx")

print("\n")
print(data)

data2 = pd.melt(data,
                id_vars = ["continent","country"],
                value_vars = ["first","third","second"])

print("\n")
print(data2)


data3 = data2.pivot(index = "country", columns = "variable", values  = "value")

print("\n")
print(data3)

data3.to_csv("data3.csv", index = True, index_label = "COUNTRY")