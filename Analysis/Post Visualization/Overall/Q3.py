import pandas as pd
import sys
import pandasql as q
import pylab as g

sys.__stdout__=sys.stdout

players = pd.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Overall")

q = q.sqldf

data = q("Select Overall from players")

data = data.round(2)

overall = list(data["Overall"])

a,b,c = g.hist(overall,rwidth=0.9)
cnt = 0
while cnt<len(a):
    g.text(b.item(cnt)+0.12,a.item(cnt),str(round(b.item(cnt),2))+" - "+str(a.item(cnt)))
    cnt+=1
g.xlabel("Overall Performance")
g.ylabel("Player Count")
g.title("Overall Histogram")
g.show()
