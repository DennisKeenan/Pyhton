from tokenize import Name


print("Welcome to driving license checker")
name=input("What's your name? ")
age=int(input("How old are you? "))
if age>=17:
    print(name,"You're eligible to get a driving license.")
else:
    print(name,"You're still not eligible to get a driving license.")
