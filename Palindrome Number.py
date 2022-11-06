from math import remainder


number=input("Please input the number!")
length=len(number)
number=int(number)
reversednumber=0

temporary=number
for (i) in range(length):
    remainder=number%10
    # print(remainder)
    reversednumber=reversednumber*10+remainder
    # print(reversednumber)
    number=number//10
    # print(number)

if temporary==reversednumber:
    print("The number is a palindrome")

else:
    print("The number isn't a palindrome")