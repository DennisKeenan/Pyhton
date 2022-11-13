lower=int(input("Enter the lower limit!"))
upper=int(input("Enter the upper limit!"))

for (i) in range(lower,upper+1):
    print()
    for (j) in range(1,11):
        print(i*j,end="\t")