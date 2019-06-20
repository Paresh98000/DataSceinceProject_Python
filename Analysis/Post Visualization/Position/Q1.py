#Q1
import pylab as g
import pandasql as s
import pandas as p

position_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Position")

print("Postions : ",len(set(position_d.Position))," Positions: \n",set(position_d.Position))

count = s.sqldf("select position,count(*)\"Player\" from position_d group by position;")

g.bar(count.Position,count.Player)

cnt = 0
while cnt<len(count.Position):
    g.text(count.Position[cnt],count.Player[cnt],str(count.Player[cnt]),size="large")
    cnt+=1

g.show()
