# Last updated: 15/9/2026, 11:32:46 pm
class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        sr, sc = source
        tr, tc = target

        # Same square
        if sr == tr and sc == tc:
            return 0

        # Different color → impossible
        if (sr + sc) % 2 != (tr + tc) % 2:
            return -1

        # Same diagonal → one move
        if abs(sr - tr) == abs(sc - tc):
            return 1

        # Same color, not same diagonal → always 2 moves on an 8×8 board
        return 2