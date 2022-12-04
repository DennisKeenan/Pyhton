sampleTuple=("one",1,1.0,True,True)
print(type(sampleTuple))
print(sampleTuple[0:4])
print(sampleTuple[::-1])

for i in sampleTuple:
    print(i)

print(sampleTuple.count(True))
print(sampleTuple.index(True))

print(sampleTuple+sampleTuple)

# sampleTuple2=("one") error
# sampleTuple2[0]="two"