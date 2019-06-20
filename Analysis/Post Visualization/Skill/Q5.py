#Q5

import pylab as g
import pandasql as s
import pandas as p

skill_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Skill")
club = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Club")
nation = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Nation")
name = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Name")

df = p.concat([skill_d,nation,club,name],axis=1)

##mostskille = s.sqldf("Select Nationality,avg(skill)'avg_skill' from df where skill<=2 group by Nationality Order by avg_skill limit 10;")
##mostskille = mostskille.round(2)
##g.bar(mostskille.Nationality,mostskille.avg_skill)
##g.xticks(rotation=90)
##avg1 = list(mostskille.avg_skill)
##nati = list(mostskille.Nationality)
##cnt=0
##while cnt<len(avg1):
##    g.text(cnt,avg1[cnt],str(avg1[cnt]),color="blue")
##    cnt+=1
##g.xlabel("Nation")
##g.ylabel("Average Skill Move")
##g.title("Average in Skill Move Ratting by each nation")
##
##g.show()

mostskille1 = s.sqldf("Select Club,count(*)'Player' from df where skill<=2 Group by club Order by Player desc limit 10;")
mostskille1=mostskille1.fillna("No Club Joined")
g.bar(mostskille1.Club,mostskille1.Player)
g.xticks(rotation=45)
plyer = list(mostskille1.Player)
club = list(mostskille1.Club)

cnt=0
col="black"
while cnt<len(plyer):
    g.text(cnt,plyer[cnt],str(plyer[cnt]),color=col,size="large")
    cnt+=1

g.xlabel("Club")
g.ylabel("Player Count")
g.title("Players Count in Skill Move Ratting less than 2 each Club")

g.show()


