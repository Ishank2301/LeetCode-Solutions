# Last updated: 2/10/2026, 12:28:06 am
class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((i+1)*(ord('z')-ord(c)+1) for i, c in enumerate(s))