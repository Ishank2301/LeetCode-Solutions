# Last updated: 15/9/2026, 11:34:22 pm
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums), max(nums))