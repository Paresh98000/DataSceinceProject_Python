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
##                'ShortPassing', 'ShotPower', 'Skill Moves', 'SlidingTackle',
##                'SprintSpeed', 'Stamina', 'StandingTackle', 'Strength', 'Vision',#'JoinYear','ValidYear',
##                'Volleys']].corr(), annot = True, linewidths=.5, cmap='Blues')

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

sns.countplot(x="Work Rate", data=df)
df.loc[:,'Work Rate'].value_counts()
plt.show()



