# Last updated: 15/9/2026, 11:33:03 pm
class Solution:
    def findMissingElements(self, a: List[int]) -> List[int]:
        return sorted({*range(min(a),max(a)+1)}-{*a})