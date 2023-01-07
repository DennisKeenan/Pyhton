import maskpass

usernames=["Emma",
"Noah",
"Liam",
"Olivia",
"Ethan",
"Ava",
"Isabella",
"Sophia",
"Jackson",
"Aiden"]
passwords=[654123,
456789,
789456,
321456,
123456,
987655,
654987,
123876,
789123,
456987]

print("Welcome to any-app, please login with your username and passwords.")
user=input("Username: ")
password=int(maskpass.askpass("Password: "))
if (user in usernames):
    i=usernames.index(user)
    if (password==passwords[i]):
        print("Login succesfull!")
    else:
        print("Wrong username or password!")
else:
    print("Wrong username or password!")