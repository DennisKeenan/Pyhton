height=int(input("Input height for the triangle!"))

# for (i) in range(height+1):
#     for (j) in range(i):
#         print("#",end=" ")
#     print()

for (i) in range(0,height+1,2):
    for (j) in range(1,i+1,2):
        print(j,end=" ")
    print()