#Height Weight

import pandas as data
import pandasql as sql
import pylab as g
import sys

sys.__stdout__ = sys.stdout
str1 = r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Football Data New Excel Format.xlsx"#input(" Enter your data path: ")

print("Path is seted : ",str1)

players = data.read_excel(str1,"data")

query = sql.sqldf

col = players.columns

data = query("Select Name,Height,Weight from players")

height = list(data.Height)

weight = list(data.Weight)

name = list(data.Name)

def height_float(val):
    try:
        if type(val) == str:
            value = val.split("'")
            return float(value[0]+"."+value[1])
        elif type(val) == float:
            return val
        else:
            return 0
    except AttributeError as ae:
        print(ae)
        return 0

