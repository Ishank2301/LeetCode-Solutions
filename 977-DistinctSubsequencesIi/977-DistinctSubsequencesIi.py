# Last updated: 15/9/2026, 11:35:19 pm
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp,last,MOD = [1]+[0]*(len(s)), [0]*128, int(1e9+7)
        for i,c in enumerate(s, start=1):
            dp[i] = ((dp[i-1] <<1) -dp[last[ord(c)] -1]) %MOD
            last[ord(c)] = i
        return  (dp[-1] +MOD-1) %MOD
        