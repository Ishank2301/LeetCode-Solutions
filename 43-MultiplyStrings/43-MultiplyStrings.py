# Last updated: 15/9/2026, 11:37:42 pm
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
    # 1. Handle zero case
        if num1 == "0" or num2 == "0":
            return "0"
    
    # 2. Initialize result array (max size M+N)
        res = [0] * (len(num1) + len(num2))
    
    # 3. Multiply digits (right to left)
        n1, n2 = num1[::-1], num2[::-1]
        for i in range(len(n1)):
            for j in range(len(n2)):
            # Multiply digit pairs, add to position
                prod = int(n1[i]) * int(n2[j])
                res[i + j] += prod
            
            # 4. Handle carry for current and next position
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
            
    # 5. Remove leading zeros and reverse back
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return "".join(map(str, res[::-1]))
