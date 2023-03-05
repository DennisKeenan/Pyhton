secret="heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V9AAB1F8}7"
result=""

for i in range(0,len(secret),3):
    result+=secret[i+2]+secret[i+0]+secret[i+1]
    print(result)
print(result)
