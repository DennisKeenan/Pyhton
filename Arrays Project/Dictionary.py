dictionary={0:"1","key":"value",True:"Benar",7.5:False}
print(type(dictionary))
print(dictionary["key"])

# print(len(dictionary))
# print(dictionary)
# print(dictionary.keys())
# print(dictionary.values())

dictionary["key"]="value2" #changing value with keys
# print(dictionary)

dictionary[3]="test" #adding key:value
# print(dictionary)

dictionary.pop(True) #delete according to keys
# print(dictionary)

dictionary.popitem() #delete last item
# print(dictionary)

# del dictionary 

# dictionary.clear() #clear dictionary
# print(dictionary)

for key in dictionary.items():
    print(key)

dictionary2=dictionary
print(dictionary2)
