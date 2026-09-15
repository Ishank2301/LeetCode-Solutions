# Last updated: 15/9/2026, 11:35:40 pm
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total  = sum(nums)
        n = len(nums)
        for i in range(n):
            right_sum  = total - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum+= nums[i]
        return -1