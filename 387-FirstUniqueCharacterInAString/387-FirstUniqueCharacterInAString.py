# Last updated: 15/9/2026, 11:36:13 pm
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i],0)+1
        
        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i
            
        return -1
