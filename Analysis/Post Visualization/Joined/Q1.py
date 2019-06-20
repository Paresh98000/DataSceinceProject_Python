#Q1

import pandas as p
import pandasql as s
import pylab as g
import seaborn as sns

#data cleaned where date was NAN replaced by 00-Jan-00 means 1-1-1900 date

join_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Join")

df = s.sqldf("select strftime('%Y',Joined)'Year',count(*)'Player' from join_d group by year order by year")

g.bar(df.Year,df.Player)
g.title("Joined player by each year")
g.xlabel("Year")
g.ylabel("Player count")
cnt = 0
while cnt<len(df.Year):
    g.text(df.Year[cnt],df.Player[cnt],str(df.Player[cnt]))
    cnt+=1
g.xticks(rotation=90)
g.show()


df = s.sqldf("select strftime('%Y',Joined)'Year' from join_d")

file = open("join.csv","w")
cnt = 0

for x in df.Year:
    file.write(""+str(x)+"\n")
    cnt+=1

file.close()
    
