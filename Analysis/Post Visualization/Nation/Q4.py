# Q4

import pandas as p
import pandasql as sql
import pylab as g
import os

print(os.getcwd())

nation = p.read_excel(r"..\Football Data New Excel Format.xlsx","Nation")

club = p.read_excel(r"..\Football Data New Excel Format.xlsx","Club")

club_dict = {}

df_merged = p.concat([nation,club],axis=1)

club_count = df_merged.groupby(by=["Nationality"]).count().sort_values("Club",ascending=False)

count = 0

# dictionary for analysis two variable nation and clubs
dict_na_clubs = {}

nations = list(club_count.index)
clubs = list(club_count.Club)

# total nations are 164
file = open("Nation_Clubs.txt","w")

while count<164:
    dict_na_clubs.update({nations[count]:clubs[count]})
    file.write(str(nations[count])+","+str(clubs[count])+"\n")
    count+=1

file.close()
value = list(dict_na_clubs.values())
key = list(dict_na_clubs.keys())
g.bar(key[:11],value[:11])

for x in range(0,11):
    g.text(x-0.10,value[x]+0.10,str(value[x]),color="blue",fontweight="bold")

g.xticks(rotation=90)
g.title("Top 10 nations with highest clubs")
g.show()
