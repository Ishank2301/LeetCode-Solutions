# Last updated: 15/9/2026, 11:33:00 pm
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        remainder_groups = [[],[],[]]
        for num in nums:
            remainder_groups[num % 3].append(num)
        for group in remainder_groups:
            group.sort(reverse=True)

        max_sum = 0


        if len(remainder_groups[0]) >= 3:
            max_sum = max(max_sum, sum(remainder_groups[0][:3]))
        if len(remainder_groups[1]) >= 3:
            max_sum = max(max_sum, sum(remainder_groups[1][:3]))
        if len(remainder_groups[2]) >= 3:
            max_sum = max(max_sum, sum(remainder_groups[2][:3]))

        if len(remainder_groups[0]) >= 1 and len(remainder_groups[1]) >= 1 and len(remainder_groups[2]) >= 1:
            max_sum = max(max_sum, remainder_groups[0][0] +remainder_groups[1][0] + remainder_groups[2][0])
    
        return max_sum


            