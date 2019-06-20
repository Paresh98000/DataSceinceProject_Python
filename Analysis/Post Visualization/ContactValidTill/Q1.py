#Q1

import pandas as p
import pandasql as s
import pylab as g

validtill_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","ContactValidTill")

list_yr=[]

from datetime import datetime as dt

a = dt(2018,4,14)
file = open("valid.csv","w")
cnt = 0
for x in validtill_d.ValidTill:
    if type(x) == type(a):
        list_yr.append(x.year)
        file.write(str(x.year)+","+str(cnt)+"\n")
        cnt+=1
    else:
        list_yr.append(x)
        file.write(str(x)+","+str(cnt)+"\n")
        cnt+=1
        
file.close()
a,b,c = g.hist(list_yr,list(range(2017,2027)))

cnt = 0

while cnt<len(a):
    g.text(b.item(cnt),a.item(cnt)+0.10,str(int(b.item(cnt)))+" - "+str(int(a.item(cnt))),fontweight="bold",size="large")
    cnt+=1

g.title("Players Contact Valid Till and Player demand in year")
g.xlabel("Years")
g.ylabel("Player Demand")
g.show()

