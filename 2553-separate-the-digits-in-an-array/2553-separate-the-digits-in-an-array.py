class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        # cnt = defaultdict(list)
        # for key, val in enumerate(nums):
        #     st = str(val)
        #     cnt[key].append(list(st))
        # ans = [int(x) for value in cnt.values() for pair in value for x in pair]
        # return ans 
        res = []
        for ch in nums:
            res.extend(int(d) for d in str(ch))
        return res


        

            
            
            