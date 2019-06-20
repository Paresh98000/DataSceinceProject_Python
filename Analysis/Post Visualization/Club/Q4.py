#Q4

import pandas as p
import pandasql as sql
import pylab as g

club_d = p.read_excel(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Football Data New Excel Format.xlsx","Club")
wage_d = p.read_excel(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Football Data New Excel Format.xlsx","Wage")

tmp = []

tmp = p.concat([club_d,wage_d],axis=1)

tmp1 = tmp.groupby("Club").sum()

tmp2 = tmp1.sort_values(ascending=False,by="Wage")

x = list(tmp2.index)
y = list(tmp2["Wage"])

tmp = []

for t in y:
    tmp.append(t/1000)

g.xticks(rotation=90)

g.ylabel("Milion Euros")

g.xlabel("Clubs")

g.title("Total wage of Club players")

c=0

while c<11:
    g.text(c,y[c],str(y[c]))
    c+=1
g.bar(x[:11],y[:11])

g.show()
