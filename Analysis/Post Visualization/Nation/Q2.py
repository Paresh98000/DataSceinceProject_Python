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

# Query 2 starts from here

pl_dict = {}
for u_n in un_na:
    count = 0
    for n in nation:
        if n == u_n:
            count+=1
    pl_dict.update({u_n:count})

# x is nation name
x = list(pl_dict.keys())
# y is player count
y = list(pl_dict.values())
g.bar(list(range(1,165)),y)
## count = 1
## while count < 165 :
##    g.bar(count,y[count-1])
##    count += 1
## g.legend(x)
g.title("Total player from each Nation")
g.savefig(".\\Total_Payers Each Nation.png")
# g.show()
g.close()
g.barh(list(range(1,165)),y)
g.title("Total player from each Nation")
g.savefig(".\\Total_Payers H Bar.png")
# g.show()
g.close()

# sorting dictionary in python

def srt(d,base="k|v",reversed1=False):
    assert type(d)==dict,"Dictionary argument is required"
    assert base.upper()=="K|V" or base.upper()=="K" or base.upper()=="V", "enter valid \"base\" argument"

    sorted_dict = {}

    if base.upper()=="K|V" or base.upper()=="K":
    
        for x in sorted(d.keys(),reverse=reversed1):
            sorted_dict.update({x:d[x]})
            print(x)
    else:

        empty_dict = {}
        
        for x in d:
            empty_dict.update({d[x]:x})

        for x in sorted(empty_dict,reverse=reversed1):
            sorted_dict.update({empty_dict[x]:x})

    return sorted_dict

sorted_nation = srt(pl_dict,"v",False)
file = open("nation_player_ascending.txt","w")
for x in sorted_nation:
    file.write(str(x)+","+str(sorted_nation[x])+"\n")
file.close()
sorted_nation = srt(pl_dict,"v",True)
file = open("nation_player_descending.txt","w")
for x in sorted_nation:
    file.write(str(x)+","+str(sorted_nation[x])+"\n")
file.close()
