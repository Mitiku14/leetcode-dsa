class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        miss = []
        last = arr[n-1]
        s = set(arr)
        for i in range(1, last + 1):
            if i not in s:
                miss.append(i)
        miss_len = 0
        if k > len(miss):
            miss_len = k - len(miss)
        for i in range(miss_len):
            miss.append(last + (i + 1))
        return miss[k-1]
        
