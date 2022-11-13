from operator import index
from pickletools import read_int4


words=input("Insert the word!") 
reversedword=""

for (i) in reversed(range(len(words))):
    reversedword+=(words[i])
print(reversedword)

palindrome=True 
index=len(words)-1
for (i) in words:
    if not i==reversedword[index]:
        palindrome=False
        break
    else:
        index-=1

if palindrome:
    print("The word is a palindrome")

else:
    print("The word isn't a palindrome")