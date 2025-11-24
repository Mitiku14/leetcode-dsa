class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        sub = ""
        res = []
        for num in nums:
            sub += str(num)
            decimal = int(sub, 2)
            res.append(decimal % 5 == 0)
        return res
        

