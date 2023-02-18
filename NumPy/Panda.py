import pandas as Pd

# data={"apple":[3,2,0,1],"orange":[6,7,0,3],"banana":[9,5,1,4]}
# purchase_data=Pd.DataFrame(data,index=["Monday","Tuesday","Wednesday","Thursday"])
# print(purchase_data)
# print(purchase_data.loc[""])

# stock_data=Pd.read_csv("Stock Markets.csv",index_col=0)
# stock_data=(stock_data.tail(28))
# print(stock_data.shape)

# stock_data=Pd.read_csv("Stock Markets.csv",index_col=0)
# row=(stock_data.shape[0])
# stock_data.drop_duplicates(inplace=True,keep="last")
# print(stock_data.shape[0]-row)

stock_data=Pd.read_csv("Stock Markets.csv",index_col=0)
stock_data.drop_duplicates(inplace=True,keep="first")
stock_data.rename(columns={"United Arab Emirates":"UEA"},inplace=True)
# print(stock_data.columns)
# print(stock_data)

# temp=range(1,79)
# stock_data.columns=temp
# print(stock_data.columns)

# stock_data.columns=[i.lower() for i in stock_data.columns]
# print(stock_data.columns)

stock_data=(stock_data.tail(28))
# print(stock_data.isnull().sum())
# stock_data.dropna(inplace=True,axis=1)
print(stock_data)

stock=stock_data["UEA"]
stock.fillna(0,inplace=True)
print(stock)

print(stock.mean())
print(stock.median())
print(stock.mode())

