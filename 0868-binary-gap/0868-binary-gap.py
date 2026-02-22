class Solution:
    def binaryGap(self, n: int) -> int:
        # bin_n = bin(n)
        # print(bin_n)
        bin_n = ""
        while n > 0:
            bin_n = str(n % 2) + bin_n
            n //= 2
        k = -1
        max_1 = 0
        for i in range(len(bin_n)):
            if bin_n[i] == '1':
                if k != -1:
                    max_1 = max(max_1, i - k)
                k = i
        
        return max_1

            

