# Last updated: 15/9/2026, 11:35:57 pm
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count,max1 = 0,0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                max1 = max(max1,count)
            else:
                count = 0
        return max1
