import pandas as pd
import sys
import pandasql as q
import pylab as g

sys.__stdout__=sys.stdout

players = pd.read_excel(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Football Data New Excel Format.xlsx","data")

q = q.sqldf

data = q("Select Nationality,count(*) as \"Players\" from players group by Nationality order by Players desc;")

#file = pd.ExcelWriter(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Nationa Wise player sum.xls")

file = open("Nationa Wise player sum.txt","w")

#data.to_excel(file,sheet_name="Sheet2")

name = list(data["Nationality"])
p_count = list(data["Players"])

g.pie(p_count,shadow=True,autopct="%.2f",startangle=90)
g.legend(name)
g.title("Top 20 Nation Wise Total Players")
g.show()
