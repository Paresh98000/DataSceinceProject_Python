import pandas as p
import pandasql as sql
import pylab as g

# reading data
club_data = p.read_excel(r"..\..\Football Data New Excel Format.xlsx","Club")

player_count = sql.sqldf("Select club,count(club)\"Players\" from club_data group by club order by Players desc")

print(player_count)

count_list = list(range(18,35))
hist_freq = list(player_count["Players"])
x,y,z=g.hist(hist_freq,count_list)
for i in range(0,len(count_list)-1):
    g.text(count_list[i]+0.25,x[i]+1,str(x[i]))
    
g.title("Clubs count in freqency of number of player")

g.show()
