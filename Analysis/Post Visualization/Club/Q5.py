#Q5

import pandas as p
import pandasql as sql
import pylab as g

club_d = p.read_excel(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Football Data New Excel Format.xlsx","Club")
wage_d = p.read_excel(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Football Data New Excel Format.xlsx","Wage")
overall_d = p.read_excel(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Football Data New Excel Format.xlsx","Overall")

df = p.concat([club_d,wage_d,overall_d],axis=1)

conclusion = sql.sqldf("Select Club,avg(Overall)\"Overall\",(sum(Wage)/100.00)\"All_Wage\" from df group by club order by All_Wage desc")

conclusion = conclusion.round(2)

x = list(conclusion["Club"])
y = list(conclusion["Overall"])
z = list(conclusion["All_Wage"])

g.xticks(range(11),rotation=90,labels=x[:11])

for i in range(0,11):
    g.bar(i-0.20,y[i],color="red")
    g.text(i-0.10,y[i],str(y[i]),color="Red",weight="bold")
    g.bar(i+0.20,z[i],color="green")
    g.text(i+0.10,z[i],str(z[i]),color="green",weight="bold")
g.title("Average Overall Performance of Club (1-100) Vs. Wage (Lakh Euros)")
g.legend(["Overall","Wage"])
g.show()
