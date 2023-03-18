import numpy as np
import matplotlib.pyplot as mp
import pandas as pd

soccer_data=pd.read_csv("soccer21-22.csv")
print(soccer_data.head())
print(soccer_data.shape)

print(soccer_data["Referee"].value_counts()) #Match Referee Frequency
print(soccer_data["HomeTeam"].value_counts()) # Home Team Frequency
print(soccer_data["HomeTeam"].corr()) # Max Goals

# mp.figure(figsize=(5,5))
# # mp.bar(soccer_data["Referee"].value_counts()[:5].keys(),soccer_data["Referee"].value_counts()[:5])
# mp.show()