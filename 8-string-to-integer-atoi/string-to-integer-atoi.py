class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        i = 0
        n = len(s)
        sign = 1
        num = 0

        # Handle sign
        if i < n and s[i] in ['+', '-']:
            if s[i] == '-':
                sign = -1
            i += 1

        # Read digits
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # Apply sign
        num = sign * num

        # Clamp
        return max(-2**31, min(num, 2**31 - 1))