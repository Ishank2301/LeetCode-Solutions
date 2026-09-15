# Last updated: 15/9/2026, 11:32:49 pm
class Solution:
    def uniformArray(self, A: list[int]) -> bool:
        return not (min(A) ^ reduce(or_, A)) & 1