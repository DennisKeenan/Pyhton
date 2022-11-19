text=input("Write any string/text: ")
countlower=countupper=countdigit=countspecial=countercharachter=0
for i in text:
    # print(i)
    if i.isalpha():
        countercharachter+=1
    if i.islower():
        countlower+=1
    elif i.isupper():
        countupper+=1
    elif i.isdigit():
        countdigit+=1
    else:
        countspecial+=1
        
print(countlower,countupper,countdigit,countspecial)
print(countercharachter)