class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length=len(nums)
        filterlist=[]
        k=1
        for i in range(length-1):
            if (nums[i]!=nums[i+1]):
                k+=1
                filterlist.append(nums[i])
                if i+1==length-1:
                    filterlist.append(nums[i+1])
        nums=filterlist
        print(nums)
        return(k)