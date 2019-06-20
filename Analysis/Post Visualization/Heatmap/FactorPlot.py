import pandas as p
import pandasql as s
import matplotlib.pyplot as plt
import seaborn as sns

df = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx","data")

##plt.rcParams['figure.figsize']=(25,16)
##hm=sns.heatmap(df[['Age', 'Overall', 'Potential', 'Value', 'Wage',
##                'Acceleration', 'Aggression', 'Agility', 'Balance', 'BallControl', 
##                'Body Type','Composure', 'Crossing','Dribbling', 'FKAccuracy', 'Finishing', 
##                'HeadingAccuracy', 'Interceptions','International Reputation',
##                'Joined', 'Jumping', 'LongPassing', 'LongShots',
##                'Marking', 'Penalties', 'Position', 'Positioning',
##                'ShortPassing', 'ShotPower', 'Skill Moves', 'SlidingTackle',#'WeightLbs',
##                'SprintSpeed', 'Stamina', 'StandingTackle', 'Strength', 'Vision',#'JoinYear','ValidYear',
##                'Volleys']].corr(), annot = True, linewidths=.5, cmap='Blues')
##
##hm.set_title(label='Heatmap of dataset', fontsize=20);
##plt.show()

##
##f,ax = plt.subplots(figsize=(25, 25))
##sns.heatmap(df.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
##plt.show()
##

##sns.swarmplot(x="Dribbling", y="Finishing",hue="Preferred Foot",data = df, color = 'red')
##plt.xticks(rotation=90)
##plt.show()

##

##sns.swarmplot(x="Position", y="Finishing",hue="Preferred Foot", data=df)
##plt.xticks(rotation=90)
##plt.show()

##sns.countplot(x="Age", data=df)
##df.loc[:,'Age'].value_counts()
##plt.show()

##sns.factorplot("Skill Moves","BallControl",data=df)
##plt.show()
##
##sns.factorplot("Age","Potential",data=df)
##plt.show()
##
##a,axis = plt.subplots(1,3)

##sns.factorplot("Weak Foot","Wage",data=df,ax=axis[0])
##
##sns.factorplot("Skill Moves","Wage",data=df,ax=axis[1])
##
##sns.factorplot("International Reputation","Wage",data=df,ax=axis[2])

##plt.show()

# -------------------------------
## Free kick
# -------

plt.plot(df.FKAccuracy,df.Curve,"bo",markersize=10);plt.plot(df.FKAccuracy,df.LongShots,"ro",markersize=5);plt.plot(df.FKAccuracy,df.Finishing,"go",markersize=3);plt.legend(["Curve","LongShots","Finishing"]);plt.xlabel("Free Kick Accuracy");plt.ylabel("Curve | LongShots | Finishing")

sns.lineplot(df.FKAccuracy,df.FKAccuracy);sns.lineplot(df.FKAccuracy,df.Curve);sns.lineplot(df.FKAccuracy,df.LongShots);sns.lineplot(df.FKAccuracy,df.Finishing);plt.title("FK Accuracy Depend Curve, Finishing and Longshots");plt.legend(["FKAccuracy","Curve","LongShots","Finishing"]);plt.ylabel("FKAccuracy | Curve | LongShots | Finishing");plt.show()


sns.scatterplot( "FKAccuracy", "Curve", data = df,sizes="8");
sns.scatterplot( "FKAccuracy", "LongShots", data = df,sizes="5");
sns.scatterplot( "FKAccuracy", "Finishing", data = df,sizes="3");

sns.jointplot( "FKAccuracy", "Curve", data = df,kind="reg");
sns.jointplot( "FKAccuracy", "LongShots", data = df,kind="reg");
sns.jointplot( "FKAccuracy", "Finishing", data = df,kind="reg");


sns.lmplot( "FKAccuracy", "Curve", data = df);
sns.lmplot( "FKAccuracy", "LongShots", data = df);
sns.lmplot( "FKAccuracy", "Finishing", data = df);


reg = p.read_excel(r"C:\Users\Hp\Documents\Data Science Project\data\Football Data New Excel Format.xlsx", "Reggression" )
sns.lmplot("FKAccuracy","data",hue="type",data=reg,palette="GnBu_r",truncate=False,markers=[".",".","."])
plt.show()

##Values for palette
##Colormap Set20 is not recognized. Possible values are: Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, icefire, icefire_r, inferno, inferno_r, jet, jet_r, magma, magma_r, mako, mako_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, rocket, rocket_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, twilight, twilight_r, twilight_shifted, twilight_shifted_r, viridis, viridis_r, vlag, vlag_r, winter, winter_r
