# Last updated: 15/9/2026, 11:37:45 pm
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Place each number in its correct index
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i]-1]:
                temp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[temp - 1] = temp

        # Step 2: Find first index where number doesn't match
        # THIS must be outside the first loop
        for i in range(1, n+1):
            if i != nums[i-1]:
                return i

        return n+1  # All 1..n present, answer is n+1