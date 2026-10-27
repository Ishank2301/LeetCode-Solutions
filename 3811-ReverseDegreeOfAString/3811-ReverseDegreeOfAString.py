# Last updated: 27/10/2026, 8:47:45 pm
class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((i+1)*(ord('z')-ord(c)+1) for i, c in enumerate(s))