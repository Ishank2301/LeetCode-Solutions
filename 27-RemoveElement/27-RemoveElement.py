# Last updated: 15/9/2026, 11:38:05 pm
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        k = len(nums) - 1
        while i <= k and i < len(nums):
            if nums[i] != val:
                i += 1
            else:
                nums[i] = nums[k]
                k -= 1
        return k + 1