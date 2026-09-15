# Last updated: 15/9/2026, 11:35:25 pm
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [[rStart, cStart]]
        r, c = rStart, cStart
        
        # East, South, West, North
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        step = 0
        di = 0 # direction index
        
        while len(res) < rows * cols:
            # Increase step size after East and after West moves
            if di % 2 == 0:
                step += 1
            
            for _ in range(step):
                r += dr[di]
                c += dc[di]
                
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
                    if len(res) == rows * cols:
                        return res
            
            di = (di + 1) % 4
            
        return res
