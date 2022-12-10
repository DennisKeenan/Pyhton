class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            if nums [i] not in dict:
                dict[target-nums[i]]=i
            else:
                return dict[nums[i]],i