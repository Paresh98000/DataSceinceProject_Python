#Q6

import pylab as g
import pandasql as s
import pandas as p

skill_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Skill")

a,b,c=g.hist(skill_d.Skill,[0,1,2,3,4,5,6])

cnt = 0
while cnt<len(a):
    g.text(b[cnt],a[cnt],str(a[cnt])+" - "+str(b[cnt]))
    cnt+=1

g.title("Histogram of Players in Skill Move")
g.xlabel("Skill Move")
g.ylabel("Player Count")
g.show()
g.close()

df = s.sqldf("Select Skill,count(Skill)\"avg\" from skill_d group by Skill;")

g.pie(df.avg,autopct="%0.2f%%",labels=df.Skill)

g.title("Players Percentage in Skill Moves")

g.show()
