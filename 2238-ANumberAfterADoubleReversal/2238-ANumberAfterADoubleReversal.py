# Last updated: 15/9/2026, 11:34:09 pm
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        return num % 10 != 0
