#Clube wise players

import pandas as data
import pandasql as sql
import sys

sys.__stdout__ = sys.stdout
str1 = r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Football Data New Excel Format.xlsx"#input(" Enter your data path: ")

print("Path is seted : ",str1)

players = data.read_excel(str1,"data")

query = sql.sqldf

#print(players)

data2 = query("Select Club,count(*) as \"Total_Players\" from players group by Club order by Total_Players;")

file = open(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Player count of club.txt","wb")
clubs = list(data2["Club"])
counts = list(data2["Total_Players"])
file.write("Club,Total_Players".encode())
for x in range(0,len(clubs)):
    str1 = str(clubs[x])+","+str(counts[x])+"\n"
    file.write(str1.encode())
    
    print(str1)
#print(data2)
file.close()
#print(players["Club"][players["Club"]=="NaN"])
