# Query 1

import pandas as p
import pandasql as sql
import pylab as g

# read excel file
nation_data = p.read_excel(r"..\Football Data New Excel Format.xlsx","Nation")

# total records
# output 18207
print(nation_data.count())

# no null value data found
# output 0
nation = nation_data["Nationality"]
print(nation_data["Nationality"][nation.isna()].count())

# unique nation
# output 164
un_na = list(set(nation))
count = len(un_na)



