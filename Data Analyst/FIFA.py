import pandas as Pd
import matplotlib.pyplot as mp
import seaborn as sb

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
# print("Nationality players:")
# nationality_players=(data["nationality"].value_counts())
# for i in nationality_players.keys():
#     if len(i)>6:
#         print(i,"\t",nationality_players[i])
#     else:
#         print(i,"\t\t",nationality_players[i])
# print("_"*25,"\n")

# # 2. Top 10 countries with highest number of players
# print("Top 10 countries with highest number of players: ")
# print(nationality_players[0:10])
# mp.figure(figsize=(8,10))
# mp.bar(nationality_players[0:10].keys(),nationality_players[0:10])
# print("_"*25,"\n")

# 3. Data with only name and salary
# players_salary=data[["short_name","wage_eur"]]
# print(players_salary.head())
# # Top 5 players with highest salary
# players_salary=players_salary.sort_values(by="wage_eur",ascending=False)
# print(players_salary.head())
# mp.figure(figsize=(8,5))
# mp.bar(players_salary["short_name"][0:5],players_salary["wage_eur"][0:5],color=["red","green","blue","violet","orange"])

# 4. Players Analyst
country=data[data["nationality"]=="Portugal"]
print(country.head())
country=data[["short_name","wage_eur","age","height_cm","weight_kg","pace","shooting","defending"]]
# Top 5 Oldest Players
print("Top 5 Oldest Players")
country=country.sort_values(by="age",ascending=False)
print(country.head(5))
print("_"*75,"\n")
# Top 5 Highest Players
print("Top 5 Highest Players")
country=country.sort_values(by="height_cm",ascending=False)
print(country.head(5))
print("_"*75,"\n")
# Top 5 Heaviest Players
print("Top 5 Heaviest Players")
country=country.sort_values(by="weight_kg",ascending=False)
print(country.head(5))
print("_"*75,"\n")
# Top 5 Fastest Players
print("Top 5 Fastest Players")
country=country.sort_values(by="pace",ascending=False)
print(country.head(5))
print("_"*75,"\n")
# Top 5 Strongest Shooting Players
print("Top 5 Strongest Shooting Players")
country=country.sort_values(by="shooting",ascending=False)
print(country.head(5))
print("_"*75,"\n")
# Top 5 Defending Players
print("Top 5 Highest Defend Players")
country=country.sort_values(by="defending",ascending=False)
print(country.head(5))
print("_"*75,"\n")

mp.show()