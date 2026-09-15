# Last updated: 15/9/2026, 11:34:59 pm
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1

        for die in range(n):
            new_dp = [0] * (target + 1)
            for t in range(target + 1):
                if dp[t] == 0:
                    continue
                for face in range(1, k + 1):
                    if t + face <= target:
                        new_dp[t + face] = (new_dp[t + face] + dp[t]) % MOD
            dp = new_dp

        return dp[target]