# Last updated: 15/9/2026, 11:36:44 pm
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        for i in range(1,len(nums)):
            temp = max(nums[i], nums[i]* curr_max, nums[i]* curr_min)
            curr_min= min(nums[i], nums[i]* curr_max, nums[i]* curr_min)
            curr_max = temp
            max_prod = max(max_prod, curr_max)
        return max_prod