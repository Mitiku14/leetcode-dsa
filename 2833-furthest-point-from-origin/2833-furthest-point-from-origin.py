class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt_r = moves.count('R')
        cnt_l = moves.count('L')
        cnt_b = moves.count('_')
        return abs(cnt_r - cnt_l) + cnt_b