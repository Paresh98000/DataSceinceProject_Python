#Q1

import pandas as p
import pandasql as s
import pylab as g

loan_d = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","Loan")

loan_d=loan_d.dropna()

#Total players
len(loan_d)
#1264

#Total different Clubs
len(set(loan_d["Loaned"]))
#341

df = s.sqldf("Select count(*)\"Player\",\"Loaned\" from loan_d group by \"Loaned\" order by Player desc limit 10;")

g.title("Maximum Loaned Players from")
g.xlabel("Clubs")
g.ylabel("Players count")
g.bar(df.Loaned,df.Player)
g.show()




