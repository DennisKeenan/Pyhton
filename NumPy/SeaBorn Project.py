import numpy as np
import matplotlib.pyplot as mp
import seaborn as sb

sb.set()
# data=np.linspace(0,10,1000)
# mp.plot(data,np.sin(data),data,np.cos(data))
# mp.show()

# Tips Data (example)
# data=sb.load_dataset("tips")
# print(data.head())
# sb.relplot(x="total_bill",y="tip",kind="scatter",data=data) #Scatter graphs
# sb.relplot(x="total_bill",y="tip",kind="line",data=data) #Line graphs
# sb.relplot(x="total_bill",y="tip",kind="scatter",data=data,hue="time",style="sex")
# sb.relplot(x="total_bill",y="tip",kind="scatter",data=data,col="time",hue="sex")

# Flight Data
data=sb.load_dataset("flights")
print(data.head())
sb.relplot(x="year",y="passengers",data=data,kind="line",hue="month",col="month")


mp.show()