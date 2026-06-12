class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        # Initialize masks
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    digit = int(board[r][c]) - 1
                    bit = 1 << digit
                    box = (r // 3) * 3 + (c // 3)

                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[box] |= bit

        def backtrack():

            if not empty:
                return True

            # MRV: find cell with minimum possibilities
            best_idx = 0
            min_choices = 10

            for i, (r, c) in enumerate(empty):
                box = (r // 3) * 3 + (c // 3)

                used = rows[r] | cols[c] | boxes[box]

                choices = 0
                for d in range(9):
                    if not (used & (1 << d)):
                        choices += 1

                if choices < min_choices:
                    min_choices = choices
                    best_idx = i

                if min_choices == 1:
                    break

            # Choose the most constrained cell
            r, c = empty[best_idx]
            empty[best_idx], empty[-1] = empty[-1], empty[best_idx]
            empty_cell = empty.pop()

            box = (r // 3) * 3 + (c // 3)
            used = rows[r] | cols[c] | boxes[box]

            for d in range(9):

                bit = 1 << d

                if used & bit:
                    continue

                # Choose
                board[r][c] = str(d + 1)

                rows[r] |= bit
                cols[c] |= bit
                boxes[box] |= bit

                # Explore
                if backtrack():
                    return True

                # Undo
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[box] ^= bit

                board[r][c] = "."

            empty.append(empty_cell)
            return False

        backtrack()
        