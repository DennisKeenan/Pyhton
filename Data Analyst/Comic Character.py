import pandas as Pd
import matplotlib.pyplot as mp
import seaborn as sb

# Load Data
data=Pd.read_csv("characters_stats.csv")

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

# Count data based on alignment
print("Chracter's aligment:")
print(data["Alignment"].value_counts())
print("_"*25,"\n")

# Filtering (Good Characters)
print("Good characters:")
good=data[data["Alignment"]=="good"]
print(good.head())
print(good.shape)
print("_"*75,"\n")
    # 1. Fastest Good Characters
print("Top 5 fastest characters:")
fast=good.sort_values(by="Speed",ascending=False)
print(fast.head(5))
print("_"*75,"\n")
    # 2. Filtering characters with maximum speed
print("Good characters with maximum speed:")
fastest=good[good["Speed"]>=100]
print(fastest)
print(fastest.shape)
print("_"*75,"\n")
  # 3. Filtering characters with minimum speed
print("Good characters with minimum speed:")
fastest=good[good["Speed"]==1]
print(fastest)
print(fastest.shape)
print("_"*75,"\n")
    # 4. Filtering characters with highest strength (strength)
print("Strongest characters:")
strongest=good[good["Strength"]>=100]
print(strongest)
print(strongest.shape)
print("_"*75,"\n")
    # 5. Filtering characters with highest stamina (power)
print("Highest stamina characters:")
stamina=good[good["Power"]>=100]
print(stamina)
print(stamina.shape)
print("_"*75,"\n")
    # 6. Filtering characters with highest durability (durability)
print("Highest durability characters:")
durability=good[good["Durability"]>100]
print(durability)
print(durability.shape)
print("_"*75,"\n")
    # 7. Sorting most powerful character (Total)
print("Most powerful characters:")
powerful=good.sort_values(by="Total",ascending=False)
print(powerful.head(30))
print("_"*75,"\n")

# Filtering (Bad Characters)
print("Bad characters:")
bad=data[data["Alignment"]=="bad"]
print(bad.head())
print(bad.shape)
print("_"*75,"\n")
    # 1. Sorting most powerful villain (Total)
print("Most powerful villains:")
powerful_bad=bad.sort_values(by="Total",ascending=False)
print(powerful_bad.head(30))
print("_"*75,"\n")


# Graphics
    # 1. Distribution speed of characters
mp.figure(figsize=(10,10))
mp.hist(data["Speed"],bins=50)
mp.title("Distribution speed of characters")
mp.xlabel("Speed")
    # 2. Iron man's piechart
ironman=data[data["Name"]=="Iron Man"]
print(ironman)
ironman_list=list(ironman.values)
print(ironman_list)
ironman_list=ironman_list[0][2:8]
print(ironman_list)
mp.pie(ironman_list)

mp.show()