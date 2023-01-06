# String Pattern Reverse ("abc,ab,a")
word=input("Input a word! ")
for i in range(len(word)):
    for k in range(len(word)-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(word[j],end=" ")
    print()
