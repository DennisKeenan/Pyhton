import csv

with open("Data.csv") as f:
    data=csv.reader(f)
    data=list(data)
    header=data[0]
    data=data[1:]
    input=input("Name of data you want to search: ")
    index=(header.index(input))
    
    count=0
    for i in data:
        if i[index]!='':
            count+=int(i[index])
    print("The total of",input,":",count)
    # for i in data:
    #     print(i)

