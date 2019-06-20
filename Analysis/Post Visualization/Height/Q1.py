#Q1
import pandas as p
import pandasql as s
import pylab as g

height_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Height")

height_d.Height.max()
# 6.9

height_d.Height.min()
# 5.1

df = s.sqldf("Select Height,count(Height)'Player' from height_d group by Height;")

g.title("Height Histogram of players")
g.xlabel("Height ( ft . inc )")
g.ylabel("Player counts")
a,b,c = g.hist(height_d.Height)
cnt = 0

while cnt<len(a):
    g.text(b.item(cnt),a.item(cnt),str(round(b.item(cnt),2))+" - "+str(a.item(cnt)),size="large",fontweight="bold")
    cnt+=1
    
g.show()
