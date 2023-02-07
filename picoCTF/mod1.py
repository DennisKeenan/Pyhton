msg=[202,137,390,235,114,369,198,110,350,396,390,383,225,258,38,291,75,324,401,142,288,397]
mod=[]
charachter=[]
result=""

for i in range(65,91):
    charachter.append(chr(i))

for i in range(0,10):
    charachter.append(str(i))

charachter.append("_")

print(charachter)

for i in msg:
    index=(i%37)
    result+=charachter[index]
print(result)