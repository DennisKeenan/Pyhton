# Pyramid String Pattern
lines=int(input("Enter number of row! "))
for i in range(lines):
    print(" "*(lines-i)+"O "*(i+1))

# Diamond String Pattern
lines=int(input("Enter number of row! "))
for i in range(lines):
    print(" "*(lines-i)+"O "*(i+1))
for i in range(lines,0,-1):
    print(" "*(lines-i+1)+"O "*(i))

# Half-Diamond String Pattern
lines=int(input("Enter number of row! "))
for i in range(lines):
    print("O "*(i+1))
for i in range(lines,0,-1):
    print("O "*(i))