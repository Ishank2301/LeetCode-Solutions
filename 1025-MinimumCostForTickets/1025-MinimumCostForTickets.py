# Last updated: 15/9/2026, 11:35:17 pm
from functools import lru_cache

class Solution:
    def mincostTickets(self, days, costs):

        @lru_cache(None)
        def dfs(i):
            if i >= len(days):
                return 0

            ans = float('inf')

            j = i
            while j < len(days) and days[j] < days[i] + 1:
                j += 1
            ans = min(ans, costs[0] + dfs(j))

            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j += 1
            ans = min(ans, costs[1] + dfs(j))

            j = i
            while j < len(days) and days[j] < days[i] + 30:
                j += 1
            ans = min(ans, costs[2] + dfs(j))

            return ans

        return dfs(0)