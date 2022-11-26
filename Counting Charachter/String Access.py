text=input("Insert the string: ")
print(text[:]) #Print all
print(text[len(text)//2]) #Print middle charachter in a string
print(text[-2]) #Print last charachter in a string
print(text[:len(text)//2+1]) #Print left-substring
print(text[len(text)//2+1:]) #Print right-substring
print(text[::-1]*30)
print(text[0::2],text[1::2],sep=" ")
