
def calculateinterest(principle,time,ROI=0.08):
    return principle*ROI*time/100
def calculatetotal(principle,interest):
    return principle+interest

principle=int(input("How much money do you have? "))
time=int(input("How long do you want to store your money (months)? "))
bank=input("Do you want to be BCA's customer? (y/n): ")
if bank=="y":
    print("Your money will be come:",calculatetotal(principle,calculateinterest(principle,time)))
else:
    ROI=float(input("What is the rate of interest in your bank (in %)? "))
    print("Your money will be come:",calculatetotal(principle,calculateinterest(principle,time,ROI)))