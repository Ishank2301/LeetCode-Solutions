# Last updated: 15/9/2026, 11:36:40 pm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return []

        cand1 = None
        count = 0
# Selection of the candidate
        for num in nums:
            if num == cand1:
                count+=1
            elif count == 0:
                cand1 = num
                count = 1
            else:
                count -= 1
# Cross validation and verification
        count = 0
        for num in nums:
            if num== cand1:
                count+=1

        n= len(nums)

        if count > n//2:
            return cand1