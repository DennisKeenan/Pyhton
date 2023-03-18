import numpy as np
import matplotlib.pyplot as mp
import seaborn as sb

sb.set()
data=sb.load_dataset("tips")
# print(data.head())
# print(data.shape)

# Seaborn Relation Plotting
# sb.relplot(x="total_bill",y="tip",kind="scatter",data=data) #Scatter graphs
# sb.relplot(x="total_bill",y="tip",kind="line",data=data) #Line graphs
# sb.relplot(x="total_bill",y="tip",kind="scatter",data=data,hue="time",style="sex")
# sb.relplot(x="total_bill",y="tip",kind="scatter",data=data,col="time",hue="sex")

# Seaborn Category Plotting
# sb.catplot(x="sex",y="total_bill",hue="smoker",jitter=0.5,data=data)
# sb.swarmplot(x="sex",y="total_bill",hue="smoker",data=data) #Removing duplicates from catplot
# sb.boxplot(x="sex",y="total_bill",hue="smoker",data=data) #Boxplot shaped data graphs
# sb.catplot(x="sex",y="total_bill",hue="smoker",data=data,kind="violin") #Violin shaped data graphs
# sb.catplot(x="sex",y="total_bill",hue="smoker",data=data,kind="boxen") #Boxen shaped data graphs


#=================================================================
# Flight Data
# data=sb.load_dataset("flights")
# print(data.head())
# sb.relplot(x="year",y="passengers",data=data,kind="line",hue="month",col="month")

# Iris Data
# data=sb.load_dataset("iris")
# print(data.head())
# sb.catplot(x="species",y="petal_length",data=data,kind="violin")
#=================================================================
mp.show()