class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length=len(nums)
        k=0
        for i in range(1,length):
            if (nums[i]!=nums[i-1]):
                k+=1
                nums[k]=nums[i]
        return(k+1)