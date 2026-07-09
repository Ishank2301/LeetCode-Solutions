import bisect

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        ends = [j[1] for j in jobs]
        n = len(jobs)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            start, end, p = jobs[i - 1]
            # find last job whose end <= this job's start
            idx = bisect.bisect_right(ends, start, 0, i - 1)
            dp[i] = max(dp[i - 1], dp[idx] + p)

        return dp[n]