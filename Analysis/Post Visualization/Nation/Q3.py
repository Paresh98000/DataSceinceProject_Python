# Q3 wage

import pandas as p
import pandasql as sql
import pylab as g
import SortDict as sd

wage_data = p.read_excel("..\\..\\Football Data New Excel Format.xlsx","Wage")
nation = p.read_excel("..\\..\\Football Data New Excel Format.xlsx","Nation")
# checking for null values
wage_data["Wage(€)"][wage_data["Wage(€)"].isna()].count()
# output is 0

#
# cleaning data
#

# renaming column
wage_data = wage_data.rename(columns={'Wage(€)':'Wage'})

# removing the k from data and making it numberik

temp_list = []

# because only first element is 0 means numeric other are of string type so it is like that...

wage = list(wage_data["Wage"])

for x in wage:
        if type(x) == str:
            temp_list.append(int(x[:-1]))
        elif type(x) == int:
            temp_list.append(x)
        else:
            temp_list.append(x)
            

wage = temp_list

# merging both data nation and wage
#
# data_merge = p.concat([nation_data,wage_data],axis=1)
# 
nation = list(nation["Nationality"])
nation_wage = {}

count=0

while count<len(nation):
    
    try:
        wage_am = nation_wage[nation[count]] + wage[count]
        nation_wage.update({nation[count]:wage_am})
    except:
        nation_wage.update({nation[count]:wage[count]})

    count+=1

file = open("Nation_Wage_Ascending.txt","w")
for x in sd.srt(nation_wage,"V"):
    file.write(str(x)+","+str(nation_wage[x])+"\n")
file.close()

nw_d=sd.srt(nation_wage,"V",True)

for x in nw_d:
        nbr = nw_d[x]
        nbr = nbr/1000
        nw_d[x]=nbr

# now wage is converted into Milion Euros

g.bar(list(nw_d.keys())[:11],list(nw_d.values())[:11])
g.title("Top 10 Nations with Wage")
g.ylabel("Million Euros")
g.xlabel("Nations")
g.show()


