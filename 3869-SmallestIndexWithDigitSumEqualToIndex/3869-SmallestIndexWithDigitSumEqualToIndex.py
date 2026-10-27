# Last updated: 27/10/2026, 8:47:37 pm
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, x in enumerate(nums):
            digitSum=0
            while x>0:
                x, r=divmod(x, 10)
                digitSum+=r
            if digitSum==i: return i
        return -1     