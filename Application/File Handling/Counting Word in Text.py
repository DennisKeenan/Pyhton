f=open("THETEXT.txt","r")
text=f.read()
count=0
input=input("Enter the word you want to search: ")
text=text.split()

for i in text:
    if i==input:
        count+=1
print("The word you searched appears", count, "times")
# print(text.count(input))