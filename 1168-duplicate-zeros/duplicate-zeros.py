class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:

        n = len(arr)
        possible_dups = 0
    # Find the number of elements that will fit in the final array
    # while counting potential zeros to duplicate.
        i = 0
        while i < n - possible_dups:
            if arr[i] == 0:
            # Handle the edge case where the last zero is the one that would 
            # overflow the array length after duplication
                if i == n - possible_dups - 1:
                    arr[n - 1] = 0 # Place the single zero at the end
                    n -= 1 # Reduce the effective length by 1 for the second pass
                    break
                possible_dups += 1
            i += 1
    
        last = n - 1 # Start from the actual last position in the modified array
    
    # Iterate backwards, filling the array
        for j in range(i - 1, -1, -1):
            if arr[j] == 0:
                arr[last] = 0
                last -= 1
                arr[last] = 0
                last -= 1
            else:
                arr[last] = arr[j]
                last -= 1

