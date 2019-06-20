#Main Analysis

#
# Read csv file converted from xlsx using Excel 2016
#
nation = read.csv("C:\\Users\\Hp\\OneDrive\\MCA\\Sem 4\\Data Science Project\\data\\Main Analysis\\Nation\\Nation.csv")

# fetching column data from dataframe
col = nation$Nationality

# Total nation counting 
len = paste("Total Nation : ", length(col))
#output 18207

print(len)

# cheking for null
nul_count=0

for(x in col){
  if(is.null(x)){
    print("Null")
    nul_count=nul_count+1
  }
}

print(paste("Null values found: ",nul_count))
#output is 0

#unique nation
u_na = unique(col)
count = length(u_na)
#output 164

freq = table(col)
barplot(df$Freq,horiz = TRUE)
title("Player on each nation")