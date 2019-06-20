#Q4

import pylab as g
import pandasql as s
import pandas as p

skill_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Skill")
nation = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Nation")

df = p.concat([skill_d,nation],axis=1)

mostskille = s.sqldf("Select Nationality,avg(skill)'avg_skill' from df group by Nationality Order by avg_skill desc limit 10;")
mostskille.round(2)
g.bar(mostskille.Nationality,mostskille.avg_skill)
g.xticks(rotation=90)
avg1 = list(mostskille.avg_skill)
nati = list(mostskille.Nationality)
cnt=0
while cnt<len(avg1):
    g.text(cnt,avg1[cnt],str(avg1[cnt]),color="blue")
    cnt+=1
g.xlabel("Nation")
g.ylabel("Average Skill Move")
g.title("Average in Skill Move Ratting by each nation")

g.show()
