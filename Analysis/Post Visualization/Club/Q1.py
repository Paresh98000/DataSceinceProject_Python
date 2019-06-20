#Q1

import pandas as p
import pandasql as sql
import pylab as g

# reading data
club_data = p.read_excel(r"..\..\Football Data New Excel Format.xlsx","Club")

# Clubs
clubs = list(club_data["Club"])

# Total
print(len(set(clubs)))
# 651
