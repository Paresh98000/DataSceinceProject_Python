#Q1
import pylab as g
import pandasql as s
import pandas as p

jersey_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Jersey")
x = set(jersey_d.Jersey)
g.hist(jersey_d.Jersey,list(x))
g.xticks(list(range(1,100)),labels=list(range(1,100)),rotation=90)
g.title("Histogram of Jersey Number")
g.show()

