class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return(strs[0])
        else:
            if len(strs[0])==0:
                return ""
            substring=""
            temp=""
            length=len(strs)
            for i in strs[0]:
                temp+=i
                for j in range(1,length):
                    if not strs[j].startswith(temp):
                        return(substring)
                substring+=i
            return(substring)

# substring=""
# listsb=[]
# if len(strs)==1:
#     return(strs[0])
# for i in strs[0]:
#     found=True
#     for j in strs:
#         if i not in j:
#             found=False
#     if found:
#         substring+=i
#     elif not found and substring!="":
#         listsb.append(substring)
#         substring=""
# if len(listsb)!=0:
#     # return(max(listsb,key=len))
#     return(listsb[0])
# else:
#     return("")