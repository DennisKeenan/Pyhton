import pandas as Pd

# data={"apple":[3,2,0,1],"orange":[6,7,0,3],"banana":[9,5,1,4]}
# purchase_data=Pd.DataFrame(data,index=["Monday","Tuesday","Wednesday","Thursday"])
# print(purchase_data)
# print(purchase_data.loc[""])

stock_data=Pd.read_csv("Stock Markets.csv",index_col=0)
stock_data=(stock_data.tail(28))
print(stock_data.shape)