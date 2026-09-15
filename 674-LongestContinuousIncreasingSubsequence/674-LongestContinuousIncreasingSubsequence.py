# Last updated: 15/9/2026, 11:35:50 pm
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        current = 1
        max_length = 1

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                current += 1
            else:
                current = 1 
            max_length = max(max_length,current)
        return max_length