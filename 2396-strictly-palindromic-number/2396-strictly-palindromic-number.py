class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        res = [bin(i)[2:] for i in range(2,n -2 + 1)]
        
        for i in range(len(res)):
            l , r = 0, len(res[i]) - 1
            s = len(res[i]) // 2
            while l <= s and l<=r:
                if res[i][l] == res[i][r]:
                    l += 1
                    r -= 1
                return False
                break
        return True


        
        


