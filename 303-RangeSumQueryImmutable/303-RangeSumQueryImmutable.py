# Last updated: 15/9/2026, 11:36:21 pm
class NumArray:

    def __init__(self, nums: List[int]):
        # Store the prefix sum
        self.nums = nums
        n  = len(nums)
        self.prefixsum = [0]*(n+1)
        for i in range(n):
            self.prefixsum[i+1] = self.prefixsum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixsum[right+1] - self.prefixsum[left]  # right is +1 because loop condition -> indexing pe focus kar.
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)