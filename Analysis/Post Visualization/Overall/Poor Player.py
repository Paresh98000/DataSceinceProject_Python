import pandas as pd
import sys
import pandasql as q
import pylab as g

sys.__stdout__=sys.stdout

players = pd.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","data")

q = q.sqldf

data = q("Select Name,Overall from players order by Overall limit 20;")

name1 = list(data["Name"])
name = []
for x in name1:
    name.append(x[:8])
overall = list(data["Overall"])

g.bar(name,overall)
g.xlabel("Players name")
g.ylabel("Overall Performance")
g.title("Poor 20 Player of the world")
g.show()
