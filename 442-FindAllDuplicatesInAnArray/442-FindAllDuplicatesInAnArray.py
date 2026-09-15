# Last updated: 15/9/2026, 11:36:06 pm
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:      # seen before → duplicate
                result.append(abs(num))
            else:
                nums[idx] *= -1    # mark as seen by negating
        return result