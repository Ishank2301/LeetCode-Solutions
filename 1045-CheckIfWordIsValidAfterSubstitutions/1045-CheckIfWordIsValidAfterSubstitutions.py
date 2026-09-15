# Last updated: 15/9/2026, 11:35:14 pm
class Solution:
    def isValid(self, s: str) -> bool:
        
        while 'abc' in s:
            s=s.replace('abc','')
        
        return s==''      