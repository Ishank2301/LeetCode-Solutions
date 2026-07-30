class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count_for_ones = 0
        count_for_zeroes = 0
        max_ones,max_zeroes = 0,0
        for i in range(len(s)):
            if s[i]=='1':
                count_for_ones += 1
                max_ones = max(max_ones,count_for_ones)
                count_for_zeroes = 0
            else:
                count_for_zeroes += 1
                max_zeroes = max(max_zeroes,count_for_zeroes)
                count_for_ones = 0 

        return max_ones>max_zeroes
         
            