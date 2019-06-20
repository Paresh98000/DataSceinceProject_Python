ft_d = Football_Data_New_Excel_Format

#ft_d



#l_m = lm(ft_d$Finishing~ft_d$Volleys)

l_m = lm(ft_d$SprintSpeed~ft_d$Acceleration+ft_d$BallControl)
l_m

tbl = summary(l_m)
tbl

plot(l_m)