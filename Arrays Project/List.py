myList=["Hello", 123, 123.0, 12.3, True]
# print(myList[-1])
myList[2]=["Ikan", False]
myList.append("World")
myList.insert(2,"Hello")
myList.remove(12.3)
count=myList.count("Hello")
# print(myList)
# print(myList[2][1])
# print(type(myList))

for i in myList:
    print(i)
print(count)
print(myList[::-1])
print(myList)
myList.reverse()
print(myList)
# print(myList[2].index(False))

myListNumber=[3,4,7,9,1,11,20,89,100]
myListNumber+=[12,51,67,99]
myListNumber.sort(reverse=True)
print(myListNumber)

myMatrixList=[[0,255,0],
             [255,0,255],
             [0,255,0]]
print(myMatrixList)

for i in myMatrixList:
    for j in i:
        print(j)

for i in range(len(myMatrixList)):
    for j in range(len(myMatrixList[i])):
        print(myMatrixList[i][j])