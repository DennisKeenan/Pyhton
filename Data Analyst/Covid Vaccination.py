import pandas as Pd
import matplotlib.pyplot as mp
import seaborn as sb
import numpy as np

# Load Data
data=Pd.read_csv("country_vaccinations.csv")

# Load Sample Data
# print("First 5 data:")
# print(data.head())
# print("_"*75,"\n")

# Load Amount of Data
# print("Amount of data:")
# print(data.shape)
# print("_"*75,"\n")

# Load Columns' Name
# print("Column name:")
# count=0
# for i in data.columns:
#     count+=1
#     print(count,i)
# print("_"*75,"\n")

# Checking null items in every columns
# print("Null items in :")
# print(data.isnull().sum())
# print("_"*75,"\n")

# Fill all null to 0
# data.fillna(value=0,inplace=True)
# print(data.isnull().sum())
# print("_"*75,"\n")

# Start and the latest date of data
# print(data["date"].min())
# print(data["date"].max())
# print("_"*75,"\n")

# Seperating date to three different columns
# date=data.date.str.split("-",expand=True)
# print(date)
# print("_"*75,"\n")

# Add columns to main data frame
# data["Year"]=date[0]
# data["Month"]=date[1]
# data["Date"]=date[2]
# data.Year=Pd.to_numeric(data.Year)
# data.Month=Pd.to_numeric(data.Month)
# data.Date=Pd.to_numeric(data.Date)
# data.date=Pd.to_datetime(data.date)
# print(data)
# print("_"*75,"\n")

# Data Info (each columns)
# print(data.info())
# print("_"*75,"\n")

# # Statistic value of columns
# print(data.mean())
# print(data.min())
# print(data.max())
print(data.describe())
# print("_"*25,"\n")

# Country counts of data
# country_count=data["country"].value_counts()
# print(country_count)
# print("_"*75,"\n")

# Graphics 
    # 1. Daily vaccinations rate
# mp.figure(figsize=(10,8))
# sb.lineplot(x=data.date,y=data.daily_vaccinations)
# mp.title("Daily Vaccinations Rate")

    # 2. Country with highest vaccinations 
country_highest_name=data.groupby("country")["total_vaccinations"].max().sort_values(ascending=False)[:10].index
print(country_highest_name)
print("_"*75,"\n")

    # 3. Highest vaccinantions rate in vaccinated countries
# highest_country=Pd.DataFrame(columns=data.columns)
# for i in country_highest_name:
#     highest_country=highest_country.append(data.loc[data["country"]==i])
# print(highest_country)
# print("_"*75,"\n")
# mp.figure(figsize=(20,8))
# sb.lineplot(x=highest_country["date"],y=highest_country["daily_vaccinations"],hue=highest_country["country"])
# mp.title("Highest vaccinantions rate in vaccinated countries")

    # 4. People with full vaccinations
# people_fully_vaccinated=data.groupby("country")["people_fully_vaccinated"].max().sort_values(ascending=False)[:25]
# print(people_fully_vaccinated)
# sb_patch=sb.barplot(x=people_fully_vaccinated,y=people_fully_vaccinated.index)
# for i in sb_patch.patches:
#     w=i.get_width()
#     h=i.get_height()
#     x=i.get_x()
#     y=i.get_y()
#     mp.text(x=w+x,y=h+y,s=w)
# print("_"*75,"\n")

    # 5. Daily vaccinations per million people
# daily_vaccinations_per_million=data.groupby("country")["daily_vaccinations_per_million"].max().sort_values(ascending=False)[:25]
# print(daily_vaccinations_per_million)
# sb_patch=sb.barplot(x=daily_vaccinations_per_million,y=daily_vaccinations_per_million.index)
# for i in sb_patch.patches:
#     w=i.get_width()
#     h=i.get_height()
#     x=i.get_x()
#     y=i.get_y()
#     mp.text(x=w+x,y=h+y,s=w)
# print("_"*75,"\n")

    # 6. Daily vaccinations in England
daily_vaccinations_england=data.query("country == England")
print(daily_vaccinations_england)
print("_"*75,"\n")

mp.show()