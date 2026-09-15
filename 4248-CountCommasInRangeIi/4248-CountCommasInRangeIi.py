# Last updated: 15/9/2026, 11:32:53 pm
class Solution:
    pow1000 = [1000, 1000000, 1000000000, 1000000000000, 1000000000000000, 1000000000000000000]
    def countCommas(self, n, k = 0):        
        for p in self.pow1000:
            k += n >= p
            
        return k * (n + 1) - (self.pow1000[k] - 1000) // 999