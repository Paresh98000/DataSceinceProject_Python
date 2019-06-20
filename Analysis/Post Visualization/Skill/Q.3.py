#Q3

import pylab as g
import pandasql as s
import pandas as p

skill_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Skill")
club = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Club")
name = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Name")

df = p.concat([skill_d,club,name],axis=1)

mostskille = s.sqldf("Select Club,count(*)'Player' from df where skill>=4 Group by club Order by Player desc limit 10;")

g.bar(mostskille.Club,mostskille.Player)
g.xticks(rotation=45)
plyer = list(mostskille.Player)
club = list(mostskille.Club)

cnt=0

while cnt<len(plyer):
    c = 0
    y = 0
    name = s.sqldf("select Name,Skill from df where skill>=4 and club=\'"+club[cnt]+"\';")
    names = list(name.Name)
    skils = list(name.Skill)
    while c<len(names):
        col = "black"
        if(cnt%2==0):
            col = "black"
            if(c==0):
                y+=0.25
        else:
            col = "black"
            if(c==0):
                y+=0.50
        y+=0.70
        g.text(cnt-0.45,y,str(names[c])+"-"+str(skils[c]),color=col,fontsize="large")
        c+=1
    g.text(cnt,plyer[cnt],str(plyer[cnt]),color=col,size="large")
    cnt+=1

g.xlabel("Club")
g.ylabel("Player Count")
g.title("Players Count in Skill Move Ratting greater than 4 each Club")

g.show()
