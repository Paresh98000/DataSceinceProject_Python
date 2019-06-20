#Q1

import pylab as g
import pandasql as s
import pandas as p

skill_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Skill")

y,x,c = g.hist(list(skill_d.Skill),[1,2,3,4,5,6])
i = 0
while i<len(y):
    g.text(x[i],y[i],str(y[i])+" players in "+str(x[i]),color="red")
    i+=1
g.xlabel("Skill Moves Rating")
g.ylabel("Players")
g.title("Players Count in Skill Move Ratting")
g.show()
