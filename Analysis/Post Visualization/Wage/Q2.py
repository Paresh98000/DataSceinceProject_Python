#Q2

#
# Data cleaned for Records where wage is not available
#

import pandas as p
import pandasql as sql
import pylab as g

wage_d = p.read_excel(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Football Data New Excel Format.xlsx","Wage")
overall_d = p.read_excel(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Football Data New Excel Format.xlsx","Overall")
name_d = p.read_excel(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Football Data New Excel Format.xlsx","Name")

df = p.concat([wage_d,overall_d,name_d],axis=1)

wage_v_overall = sql.sqldf("Select (Wage/10.00)\"Wage\", Overall, Name from df order by Wage desc")

c = 0
c1 = 0
list_x = []

while c<10:
    
    tmp = c-0.6+c1+(c+c1)
    tmp = tmp/2
    g.bar(c-0.6+c1,wage_v_overall["Wage"][c],color="green")
    g.bar(c+c1,wage_v_overall["Overall"][c],color="red")
    c+=1
    c1+=1
    list_x.append(tmp)

g.xticks(list_x,labels=wage_v_overall["Name"][0:10])
g.legend(["Wage","Performance"])
g.show()
