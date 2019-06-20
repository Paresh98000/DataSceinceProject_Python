#Q1

import pylab as g
import pandasql as s
import pandas as p

body_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","BodyType")

a,b,c = g.hist(list(body_d.BodyType))
cnt = 0

while cnt<len(a):
    g.text(b.item(cnt),a.item(cnt),str(a.item(cnt)),size="large")
    cnt+=1
    
g.xticks(rotation=90)
g.title("Histogram of Players in BodyType")
g.xlabel("Body Type")
g.ylabel("Player Count")
g.show()
