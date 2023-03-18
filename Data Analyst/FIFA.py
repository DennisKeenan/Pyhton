import pandas as Pd
import matplotlib.pyplot as Mp
import seaborn as Sb

# Load Data
data=Pd.read_csv("players_20.csv",index_col=0)

# Load Sample Data
print("First 5 data:")
print(data.head())
print("_"*25,"\n")

# Load Amount of Data
print("Amount of data:")
print(data.shape)
print("_"*25,"\n")

# Load Columns' Name
print("Column name:")
count=0
for i in data.columns:
    count+=1
    print(count,i)
print("_"*25,"\n")

# 1. Calculate total number of players according to nationality
print("Nationality players:")
nationality_players=(data["nationality"].value_counts())
for i in nationality_players.keys():
    if len(i)>6:
        print(i,"\t",nationality_players[i])
    else:
        print(i,"\t\t",nationality_players[i])
print("_"*25,"\n")

# 2. Top 10 countries with highest number of players
print("Top 10 countries with highest number of players: ")
print(nationality_players[0:10])
print("_"*25,"\n")