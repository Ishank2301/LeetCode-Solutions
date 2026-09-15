# Last updated: 15/9/2026, 11:33:53 pm
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        # well actually it is very easy you just have to calculate lenght if its str with no all element being digits if all elements are digits write the digit
        # Check for strs having digits only others can be done using an else and than len
        k = 0
        ans = 0
        for s in strs:
            is_numeric = True # Start with the assumption it's all digits
            for char in s:
                if not('0' <= char <= '9'):
                    is_numeric = False
                    break
            if is_numeric:
                k = int(s)
            else:
                k = len(s)
            
            ans = max(k,ans)
        return ans
