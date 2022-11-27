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

