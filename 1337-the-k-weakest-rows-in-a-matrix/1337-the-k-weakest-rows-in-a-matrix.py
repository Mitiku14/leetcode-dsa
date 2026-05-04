class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        cnt_sold = 0
        mapp = {}
        for i in range(n):
            cnt_sold = mat[i].count(1)
            mapp[i] = cnt_sold
        srt = sorted(mapp.items(), key=lambda x: x[1])
        res = []
        for i in range(k):
            res.append(srt[i][0])
        return res

