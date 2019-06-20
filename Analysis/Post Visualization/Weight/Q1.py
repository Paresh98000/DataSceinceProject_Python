#Q1
import pandas as p
import pandasql as s
import pylab as g

weight_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Weight")

weight_d.Weight.max()
# 243lbs

weight_d.Weight.min()
# 110lbs

df = s.sqldf("Select Weight,count(Weight)'Player' from weight_d group by Weight;")

g.title("Weight (lbs) Graph of Players")
g.xlabel("Weight (lbs) ")
g.ylabel("Player Counts")
a,b,c = g.hist(weight_d.Weight)
cnt = 0

while cnt<len(a):

    g.text(b.item(cnt),a.item(cnt),str(round(b.item(cnt),2))+"lbs - "+str(round(a.item(cnt),2)),size="small",fontweight="bold")
    cnt+=1

g.show()
