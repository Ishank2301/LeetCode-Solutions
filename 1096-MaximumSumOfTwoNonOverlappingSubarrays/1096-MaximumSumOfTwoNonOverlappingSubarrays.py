# Last updated: 15/9/2026, 11:35:12 pm

        # How do we even check if they are not overlapping and than how do we find out if they are maximum sum;)
        # Well subarray means being contigous:)
        # We have to return the sum so lets do this
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if len(A) < L + M: return 0
        for i in range(1, len(A)):
            A[i] += A[i - 1]
        res, maxL, maxM = A[L + M - 1], A[L - 1], A[M - 1]
        for i in range(L + M, len(A)):
            maxL = max(maxL, A[i - M] - A[i - M - L])
            maxM = max(maxM, A[i - L] - A[i - L - M])
            res = max(res, maxL + A[i] - A[i - M], maxM + A[i] - A[i - L])
        return res

