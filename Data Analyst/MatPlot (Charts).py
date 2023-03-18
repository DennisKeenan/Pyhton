import numpy as np
import matplotlib.pyplot as mp

# Opening
# mp.plot([1,2,3,4])
# mp.plot([1,2,3,4],[5,6,7,8],color="Maroon")

# Data
# mp.xlabel("Weight (kg)")
# mp.ylabel("Height (cm)")
# mp.xlabel("Month")
Height_min=np.array([45.6,50.0,53.2,55.8,58.0,59.9,61.5])
Weight_min=np.array([2.4,3.2,4.0,4.6,5.1,5.5,5.8])
Months=np.array(["Jan","Feb","Mar","Apr","May","Jun","Jul"])
Sales=np.array([1000,350,700,1020,2000])
Explode=[0,0,0,0,0.1]
Products=np.array(["Apple","Avocado","Tangerines","Banana","Grapes"])

# Running Code
# mp.plot(Weight_min,Height_min,color="Black",marker="o") #Lines (plot) for graphic
# mp.scatter(Weight_min,Height_min,color="Black",marker="o",s=100) #Dots (scatter) for graphic
# mp.bar(Months,Height_min,color="Black",width=0.1) #Vertical bars for graphic
# mp.barh(Months,Height_min,color="Black",height=0.1) #Horizontal bars for graphic
mp.pie(Sales,labels=Products,explode=Explode,colors=["Red","Green","Orange","Yellow","Purple"],startangle=90.0) #Piecharts
mp.legend(title="Fruits Color")
mp.show()