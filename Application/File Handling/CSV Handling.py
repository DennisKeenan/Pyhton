import csv

with open("Data.csv") as f:
    data=csv.reader(f)
    data=list(data)
    header=data[0]
    data=data[1:]

    print(header.index("deaths_civilians"))
    count=0
    for i in data:
        if i[40]!='':
            count+=int(i[40])
            print(i[40])
    print(count)
    # for i in data:
    #     print(i)

