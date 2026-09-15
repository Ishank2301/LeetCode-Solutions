# Last updated: 15/9/2026, 11:37:28 pm

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        
        # Pre-generate string templates to completely avoid inner-loop string operations
        # E.g., for n=4: [".Q..", "..Q.", ...]
        row_templates = [
            ["." * col + "Q" + "." * (n - 1 - col) for col in range(n)]
            for _ in range(n)
        ]
        
        # Pre-allocate a list to store the column placements for the current board
        current_board = [0] * n

        # Bitmask markers: 1 means attacked/blocked, 0 means open
        def backtrack(row: int, cols: int, diag1: int, diag2: int):
            if row == n:
                # Convert the column indices directly into pre-generated strings
                ans.append([row_templates[r][current_board[r]] for r in range(n)])
                return
            
            # (cols | diag1 | diag2) gives a bitmask of ALL blocked positions in this row
            # ~ negates it to flip 0s to 1s (representing valid open positions)
            # & ((1 << n) - 1) limits the bitmask precisely to our 'n' board columns
            available_positions = ~(cols | diag1 | diag2) & ((1 << n) - 1)
            
            # Loop while there are still open positions (1s) left in the mask
            while available_positions:
                # Extract the lowest set bit (isolates the rightmost '1')
                # This represents the exact column position we are testing
                position_bit = available_positions & -available_positions
                
                # Clear this bit from available positions so we don't look at it again
                available_positions ^= position_bit
                
                # Use .bit_length() - 1 to find the exact column index (0 to n-1)
                col_idx = position_bit.bit_length() - 1
                current_board[row] = col_idx
                
                # Recurse to the next row:
                # - Shift diag1 left (<< 1) because the diagonal moves left in the next row
                # - Shift diag2 right (>> 1) because the diagonal moves right in the next row
                backtrack(
                    row + 1, 
                    cols | position_bit, 
                    (diag1 | position_bit) << 1, 
                    (diag2 | position_bit) >> 1
                )

        # Start backtracking from row 0 with all masks set to empty (0)
        backtrack(0, 0, 0, 0)
        return ans
