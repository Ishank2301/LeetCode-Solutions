# Last updated: 15/9/2026, 11:36:30 pm
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0: return False
        buckets = {}
        width = valueDiff + 1
        
        for i, num in enumerate(nums):
            bucket_id = num // width # Put number into its bucket
            
            # 1. Same bucket?
            if bucket_id in buckets:
                return True
            # 2. Left bucket?
            if (bucket_id - 1) in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
            # 3. Right bucket?
            if (bucket_id + 1) in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
            
            # Add to current bucket
            buckets[bucket_id] = num
            
            # Keep window size within indexDiff
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // width]
                
        return False
