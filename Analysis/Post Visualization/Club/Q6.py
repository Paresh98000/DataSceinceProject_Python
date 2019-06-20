#Q6

import pandas as p
import pandasql as sql
import pylab as g

club_d = p.read_excel(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Football Data New Excel Format.xlsx","Club")
name_d = p.read_excel(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Football Data New Excel Format.xlsx","Name")

df = p.concat([club_d,name_d],axis=1)

# players didn't joined any club yet
unjoined = df["Name"][df["Club"].isna()].count()
# output 241

# player joined clubs
joined = df["Name"][df["Club"].isna()==False].count()
#output 17966

g.pie([joined,unjoined],labels=["Joined","Unjoined"],autopct="%.2f%%")
g.show()
