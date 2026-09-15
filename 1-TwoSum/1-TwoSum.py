# Last updated: 15/9/2026, 11:38:49 pm
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dicti = {}
        for i in range(n):
            rem = target - nums[i]
            if rem in dicti:
                return [dicti[rem],i]
            
            dicti[nums[i]] = i