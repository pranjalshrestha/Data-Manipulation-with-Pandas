'''
Pranjal Shrestha
DSC 270 - Data Manipulation
Pandas Project
'''
import pandas as pd


# 1
Q1 = pd.read_csv('wsl_2022-2023.csv')
print(Q1.to_string())
print("\n=======\n")


# 2 
num_goals = Q1["Goals"].sum()
print("The total number of Goals is:", num_goals)
print("\n=======\n")


# 3
new_Q1 = Q1.groupby('Team')['Goals'].sum()
print(new_Q1)
print("\n=======\n")


# 4
Q4 = Q1.copy()
Q4 = Q4.dropna()
print(Q4.to_string())
num_goals1 = Q4["Goals"].sum()
print("The total number of Goals is:", num_goals1)
print("\n=======\n")


# 5
Q5 = Q4.copy()
Q5 = Q5.drop_duplicates()
print(Q5.to_string())
num_goals2 = Q5["Goals"].sum()
print("The total number of Goals is:", num_goals2)
print("\n=======\n")


# 6
stats_summary = Q5.describe()
print(stats_summary.to_string())
print("\n=======\n")


# 7
bethany_indexes = Q5[Q5['Player'] == 'Bethany England'].index
print(bethany_indexes)
print("\n=======\n")


# 8
#It means there is only one row left with Bethany England after removing duplicates.
#The remaining rows with the player 'Bethany England' are unique, and there are no duplicate entries for this player.


# 9
Q9 = Q5.copy()
Q9 = Q9.set_index('Player')
print(Q9.to_string())
print("\n=======\n")


# 10
print(Q9.loc['Megan Finnigan'])
print("\n=======\n")


# 11
goals_rachel = Q9.loc['Rachel Daly', 'Goals']
print("The number of Goals for Rachel Daly is:", goals_rachel)
print("\n=======\n")


# 12
Q9['Discipline'] = 4 * (Q9['Red']) + 1 * (Q9['Yellow'])
print(Q9.to_string())


# 13
Q13 = Q9[['Team', 'Discipline']]
print(Q13)
print("\n=======\n")


# 14
Q14 = Q13.sort_values(by=['Discipline', 'Player'], ascending=[False, True])
print(Q14.to_string())
print("\n=======\n")


# 15
Q15 = Q14.groupby('Team')['Discipline'].sum()
print(Q15)
print("\n=======\n")


# 16
Q16 = Q14[Q14['Discipline'] > 0]
Q16 = Q16.sort_values(by=['Team', 'Discipline'], ascending=[True, False])
print(Q16.to_string())
print("\n=======\n")


# 17
data = {'Player': ['Beth Mead', 'Hayley Raso', 'Guro Reiten'],
        "Team": ['arsenal', 'everton', 'chelsea'],
        "Discipline": [6, None, 2]}
Q17 = pd.DataFrame(data)
Q17 = Q17.set_index('Player')
print(Q17)
print("\n=======\n")

 
# 18
avg = Q17['Discipline'].mean()
Q17['Discipline'] = Q17['Discipline'].fillna(avg)
print(Q17)
print("\n=======\n")


# 19
Q19 = pd.concat([Q16, Q17])
print(Q19.to_string())
print("\n=======\n")


# 20
def fix_name_format(name):
    return name.title()

Q19['Team'] = Q19['Team'].map(fix_name_format)
print(Q19)
print("\n=======\n")
