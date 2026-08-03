class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        # Base case: S_1 is always "0"
        if n == 1:
            return "0"
        
        # Calculate the length of S_n, which is (2^n) - 1
        length = (1 << n) - 1
        mid = (length // 2) + 1
        
        # Case 1: k is exactly the middle element
        if k == mid:
            return "1"
        
        # Case 2: k is in the first half (same as S_{n-1})
        elif k < mid:
            return self.findKthBit(n - 1, k)
        
        # Case 3: k is in the second half (reversed and inverted S_{n-1})
        else:
            # Find the mirrored index in the left half
            mirrored_k = mid - (k - mid)
            # Find the bit at the mirrored index
            original_bit = self.findKthBit(n - 1, mirrored_k)
            # Invert the bit ('0' -> '1', '1' -> '0')
            return "1" if original_bit == "0" else "0"
