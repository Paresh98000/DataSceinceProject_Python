# Q5 and Q6

import pandas as p
import pandasql as sql
import pylab as g
import os

nation = p.read_excel(r"..\Football Data New Excel Format.xlsx","Nation")

name = p.read_excel(r"..\Football Data New Excel Format.xlsx","Name")

Overall = p.read_excel(r"..\Football Data New Excel Format.xlsx","Overall")

data = p.concat([nation,name,Overall],axis=1)

# best player of nation
result = sql.sqldf("Select a.Nationality,a.Name,a.Overall from data a where Overall = (Select Max(Overall) from data b where a.Nationality=b.Nationality) order by Nationality")

uni_nation = list(set(result["Nationality"]))
uni_nation.sort()
dict_players_of_nation = {}
dict_players_overall = {}
file = open("Nation_Best_Player.txt","wb")
file1 = open("Nation_Overall_Max.txt","wb")
for x in uni_nation:

    list1 = []
    for y in list(result["Name"][result["Nationality"]==x]):
        list1.append(y)
        
    dict_players_of_nation.update({x:list1})
    dict_players_overall.update({x:list(result["Overall"][result["Nationality"]==x])[0]})
    file.write((str(x)+","+str(list1)+"\n").encode())
    file1.write((str(x)+","+str(list(result["Overall"][result["Nationality"]==x])[0])+"\n").encode())

file.close()
file1.close()

import SortDict as sd

dict_players_overall = sd.srt(dict_players_overall,"V",True)

x = list(dict_players_overall.keys())
y = list(dict_players_overall.values())

g.bar(x[:11],y[:11])
g.xticks(rotation=90)
count = 0
while count<11:
    g.text(count,y[count]+1,str(y[count]))
    count+=1
g.title("Top 10 Nation by Overall Performance of their best player")
g.show()
