class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3:
            return False
        target = total // 3
        cnt = 0
        cur = 0
        for num in arr:
            cur += num
            if cur == target:
                cnt += 1
                cur = 0
        
        return cnt >= 3

