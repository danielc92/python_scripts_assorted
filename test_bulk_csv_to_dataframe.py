import pandas as pd
import requests
import glob

#csvs must have same headers

path = 'H:/Data/daniel_corcoran_python_projects/datasets/TESTBULK/'

all_files = glob.glob(path + "*.csv")

frame = pd.DataFrame()

list = []

for file in all_files:
    df = pd.read_csv(file, index_col = None, header = 0)
    list.append(df)

frame = pd.concat(list)

print(frame)

print(all_files)

frame.to_csv("all_crypto_2018-02-07.csv", index = False)