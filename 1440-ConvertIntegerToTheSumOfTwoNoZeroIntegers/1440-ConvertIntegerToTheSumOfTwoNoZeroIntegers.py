# Last updated: 15/9/2026, 11:34:54 pm
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n):
            a = i
            b = n - i 
            if "0" not in str(a) and "0" not in str(b):
                return [a,b]