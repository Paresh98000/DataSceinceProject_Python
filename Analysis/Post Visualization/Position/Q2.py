#Q2
import pylab as g
import pandasql as s
import pandas as p

position_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Position")
wage_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Wage")

df = p.concat([position_d,wage_d],axis=1)

count = s.sqldf("select position,sum(wage)\"Wage\" from df group by position;")

count= count.fillna("NAN")

g.bar(count.Position,count.Wage)


cnt = 0

while cnt<len(count.Position):
    g.text(count.Position[cnt],count.Wage[cnt],str(count.Wage[cnt]),size="large")
    cnt+=1

g.show()
