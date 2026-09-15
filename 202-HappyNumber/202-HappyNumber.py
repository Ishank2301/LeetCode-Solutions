# Last updated: 15/9/2026, 11:36:37 pm
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = self.next_number(n)

        return True

    def next_number(self, n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total
