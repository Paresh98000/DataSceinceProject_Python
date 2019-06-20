#Q1 in Wage total Wage of all players

import pandas as p
import pandasql as sql
import pylab as g

wage_d = p.read_excel(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Football Data New Excel Format.xlsx","Wage")

#total wage

total_wage = float(wage_d.sum())

total_wage = total_wage/1000

print("Total wage of all fifa players is ",total_wage," Million Euros")

