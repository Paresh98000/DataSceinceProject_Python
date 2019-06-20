#Q1

import pylab as g
import pandasql as s
import pandas as p

reputation_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Reputation")

y,x,c = g.hist(list(reputation_d.Reputation),[1,2,3,4,5,6])
i = 0
while i<len(y):
    g.text(x[i],y[i],str(y[i])+" players in "+str(x[i]),size="large",fontweight="bold")
    i+=1
g.xlabel("International Reputation Rating")
g.ylabel("Players")
g.title("Players Count in International Reputation Ratting")
g.show()
