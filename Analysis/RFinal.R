data_file = read.csv("C:\\Users\\Hp\\Documents\\Data Science Project\\data\\Post Visualization\\Joined\\join.csv")

x = lm(data_file$year~data_file$player)
x

ycap = fitted(x)

ycap

data_file