#Q1
import pandas as p
import pandasql as s
import pylab as g

age_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Age")

age_d.Age.max()
# 46

age_d.Age.min()
# 16

df = s.sqldf("Select Age,count(Age)'Player' from age_d group by Age;")

g.title("Age Graph of players")
g.xlabel("Age")
g.ylabel("Player counts")
g.bar(df.Age,df.Player)
g.xticks(ticks=list(range(16,47)),labels=list(range(16,47)))
g.show()
