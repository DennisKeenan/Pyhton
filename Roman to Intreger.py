class Solution:
    def romanToInt(self, s: str) -> int:
        s=s.replace("IV","IIII").replace("IX","VIIII").replace("XL","XXXX").replace("XC","LXXXX")
        s=s.replace("CM","DCCCC").replace("CD","CCCC")
        result=0
        for i in s:
            if i=="I":
                result+=1
            elif i=="V":
                result+=5
            elif i=="X":
                result+=10
            elif i=="L":
                result+=50
            elif i=="C":
                result+=100   
            elif i=="D":
                result+=500
            else:
                result+=1000
        return result