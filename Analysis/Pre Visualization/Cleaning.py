import pandas as data
import pandasql as sql
import codecs as cd
import sys

sys.__stdout__ = sys.stdout
str1 = r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Football Data New Excel Format.xlsx"#input(" Enter your data path: ")

print("Path is seted : ",str1)

players = data.read_excel(str1,"data")

query = sql.sqldf

col = players.columns

start = 28

end = 53

data = players.dropna(subset=col[start:end])

print(data)

#rows 16122

file = cd.open(r"C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data\Performance.csv",encoding="utf-8",mode="w")

for x in data:
    file.write((str(x)+","))
file.write("\n")
for x in range(0,len(data)):
    error = False
    for xx in range(0,len(col)):
        try:
            file.write((str(data[col[xx]][x])+","))
            
        except KeyError as ke:
            error = True
            #print("Key Error player not found: ",ke)
            break
        except Exception as e:
            error = True
            print("Error Occured at: ","X: ",x," XX: ",xx," -> ",e)
            break
    if error==False:
        file.write("\n")

file.close()



