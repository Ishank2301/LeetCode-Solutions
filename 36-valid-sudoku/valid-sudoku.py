class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # The board is cinsidered a matrix with partitions having 3*3 matrix with these matrix creating a 3*3


        # Let's make the  hashmap for this to be converted into sudoku:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]



        # we should check for the number in the row and column of every matrix

        for r in range(9):
            for c in range(9): 
                val = board[r][c]

            # Skip the empty cell:    
                if val == ".":
                    continue


            # Determine which box does the cell belong to :
                box = (r//3)*3 + (c//3)
                
            # Determine which elements are duplicate:
                if val in rows[r]:
                    return False

                if val in cols[c]:
                    return False

                if val in boxes[box]:
                    return False

            # Mark as seen:
                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)
        return True
