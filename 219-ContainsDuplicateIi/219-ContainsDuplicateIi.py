# Last updated: 15/9/2026, 11:36:32 pm
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):  # Enumerate to get both key and count value pair
            if num in seen:
                if i - seen[num] <= k: # seen[num] represent prev_indices
                    return True

            seen[num] = i  # Replace it with the curr_indices
        return False
