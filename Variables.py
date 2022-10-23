from tokenize import Special
from xmlrpc.client import boolean

# Text
string="Hello Earth"
mlString="Hello\nEarth\"\'\\\t x\b\rikan"
numberString="1234567890"
print(type(numberString),type(mlString),type(string))

# Value
numbers=123
float=1.5
negativeNumbers=-123
boolean=True
Special=None
print(type(numbers),type(negativeNumbers),type(float),type(boolean),type(Special))

# Collection
list=[1,2,3,1.5,"hello",boolean]
tuple=(1,2,3,1.5,"hello",boolean)
dictionary={1:"one",2:"two","three":3}
print(type(list),type(tuple),type(dictionary))

# Operator
print(numbers+negativeNumbers)
print(numbers+float)
print(string+numberString)
print(numbers+int(numberString))
print(numbers-negativeNumbers)
print(numbers-float)
# print(string-numberString) -> Invalid
print(numbers-int(numberString))
print(numbers*negativeNumbers)
print(numbers*float)
# print(string*numberString) -> Invalid
print(numbers*int(numberString))
print(4*string)
print(numbers/negativeNumbers)
print(numbers/float)
# print(string/numberString) -> Invalid
print(numbers/int(numberString))
print(numbers%negativeNumbers)
print(17%5)
print(17//5)
numbers+=12
print(numbers)
numbers-=100
print(numbers)
numbers*=2
print(numbers)
numbers/=2
print(numbers)
numbers%=6
print(numbers)
numbers//=2
print(numbers)