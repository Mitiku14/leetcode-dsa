class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1
        s = [1, 2, 2]
        head  , num = 2, 1
        count_ones = 1
        while len(s) < n:
            repeat = s[head]
            s.extend([num] * repeat) 
            if num == 1:
                count_ones += min(repeat, n - len(s) + repeat)
            num = 3 - num
            head += 1
        return count_ones



