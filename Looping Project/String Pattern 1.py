# String Pattern ("a,bb,ccc")
word=input("Input a word! ")
for i in range(len(word)):
    for j in range(i+1):
        print(word[i],end=" ")
    print()

# String Pattern ("a,ab,abc")
word=input("Input a word! ")
for i in range(len(word)):
    for j in range(i+1):
        print(word[j],end=" ")
    print()

# String Pattern Reverse ("abc,ab,a")
