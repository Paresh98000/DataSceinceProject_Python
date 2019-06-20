#Q1
import pylab as g
import pandasql as s
import pandas as p

wfoot_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","WeakFoot")

y,x,c = g.hist(list(wfoot_d.WeakFoot),[1,2,3,4,5,6])
i = 0
while i<len(y):
    g.text(x[i],y[i],str(y[i])+" players in "+str(x[i]),fontweight="bold",size="large")
    i+=1
g.xlabel("Weak Foot Rating")
g.ylabel("Players")
g.title("Players Count in Weak Foot Ratting")
g.show()
