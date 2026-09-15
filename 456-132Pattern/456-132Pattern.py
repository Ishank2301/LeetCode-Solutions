# Last updated: 15/9/2026, 11:36:02 pm
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = None

        for n in reversed(nums):
            if third and n < third:
                return True

            while stack and n > stack[-1]:
                third = stack.pop()

            stack.append(n)

        return False