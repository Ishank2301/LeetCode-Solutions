# Last updated: 15/9/2026, 11:32:58 pm
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        seen  = set()
        #Tranverse from left to right
        for i in range(n-1,-1,-1):
            if nums [i] in seen:
                operations_needed = (i+1+2) // 3
                return operations_needed
            seen.add(nums[i])
        return 0