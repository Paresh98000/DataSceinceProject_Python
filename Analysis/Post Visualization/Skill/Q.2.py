#Q2

import pylab as g
import pandasql as s
import pandas as p

skill_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Skill")
nation = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Nation")

df = p.concat([skill_d,nation],axis=1)

mostskille = s.sqldf("Select Nationality,count(*)'Player' from df where skill>=4 group by Nationality Order by Player desc limit 10;")

g.bar(mostskille.Nationality,mostskille.Player)
g.xticks(rotation=90)
plyer = list(mostskille.Player)
nati = list(mostskille.Nationality)
cnt=0
while cnt<len(plyer):
    g.text(cnt,plyer[cnt],str(plyer[cnt]),color="blue")
    cnt+=1
g.xlabel("Nation")
g.ylabel("Player Count")
g.title("Players Count in Skill Move Ratting by each nation")

g.show()
