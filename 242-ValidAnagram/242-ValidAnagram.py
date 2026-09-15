# Last updated: 15/9/2026, 11:36:24 pm
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s)!=len(t):
            return False

        # We have to use the Increment Decrement Pointer in this shi
        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i],0) + 1
            seen[t[i]] = seen.get(t[i],0) - 1

        for num in seen.values():
            if num!=0:
                return False
        return True        