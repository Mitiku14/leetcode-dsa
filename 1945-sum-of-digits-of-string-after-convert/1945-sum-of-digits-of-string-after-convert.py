class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp = {chr(97 + i): (i + 1) for i in range(26)}
        st = ""
        for sx in s:
            t = temp[sx]
            st += str(t)
        res = 0
        for i in range(k):
            res = sum(int(sy) for sy in st)
            st = str(res)
        return res

            

