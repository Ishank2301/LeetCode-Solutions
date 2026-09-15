# Last updated: 15/9/2026, 11:38:06 pm
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        n = len(nums)
        if n==0:
            return 0
        for i in range(1,n):
            if nums[i]!=nums[j]:
                j+=1
                nums[j] = nums[i]
        return j+1

