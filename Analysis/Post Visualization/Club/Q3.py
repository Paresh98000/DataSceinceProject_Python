#Q3

import pandas as p
import pandasql as sql
import pylab as g

club_d = p.read_excel(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Football Data New Excel Format.xlsx","Club")
overall_d = p.read_excel(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Football Data New Excel Format.xlsx","Overall")

merge = p.concat([club_d,overall_d],axis=1)

avg = merge.groupby("Club").mean()

avg = avg.sort_values("Overall",ascending=False)

club1 = list(avg.index)

overall1 = list(avg["Overall"])

g.bar(club1[:11],overall1[:11])
g.xticks(rotation=45)
count = 0

while count<11:
    g.text(count,overall1[count],str(round(overall1[count],2)))
    count+=1
    
g.show()
