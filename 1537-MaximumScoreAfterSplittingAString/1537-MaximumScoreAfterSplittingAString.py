# Last updated: 15/9/2026, 11:34:50 pm
class Solution:
    def maxScore(self, s: str) -> int:
        # Split the score is counted as how many 0's are in left and how many 1's are in right

        # Precompute the prefix_sums of '1'.
        n = len(s)
        count = 0 #  'total "1" '.
        zer = 0 # '0' on left
        ones = 0 # '1' on left
        max_score = -float(inf)
        one_sum = [0]*n
        for i in range(n):
            if s[i]=='1':
                count+=1
        for i in range(n-1):
            if s[i] == '0':
                zer+=1
            else:
                ones+=1
            curr_score = count + (zer-ones)
            max_score = max(max_score,curr_score)
        return max_score
