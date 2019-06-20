import pylab as g
import pandasql as s
import pandas as p

face_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","RealFace")

df = s.sqldf("select RealFace,count(*)\"Total\" from face_d group by RealFace;")

g.title("Real Face of Players")
g.pie(df.Total,labels=df.RealFace,autopct="%.2f%%")
g.show()
