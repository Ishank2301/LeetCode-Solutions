from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # Precompute powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # Prefix arrays
        digit_sum = [0] * (n + 1)
        non_zero_cnt = [0] * (n + 1)
        prefix_num = [0] * (n + 1)

        for i, ch in enumerate(s, 1):
            d = int(ch)
            digit_sum[i] = digit_sum[i - 1] + d
            non_zero_cnt[i] = non_zero_cnt[i - 1] + (d != 0)

            if d != 0:
                prefix_num[i] = (prefix_num[i - 1] * 10 + d) % MOD
            else:
                prefix_num[i] = prefix_num[i - 1]

        ans = []

        for l, r in queries:
            cnt = non_zero_cnt[r + 1] - non_zero_cnt[l]
            sm = digit_sum[r + 1] - digit_sum[l]

            x = (
                prefix_num[r + 1]
                - prefix_num[l] * pow10[cnt]
            ) % MOD

            ans.append((x * sm) % MOD)

        return ans