class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = defaultdict(list)
        strs.sort()
        for ch in strs:
            temp = sorted(ch)
            cnt[''.join(temp)].append(ch)
        res = []
        for key, val in cnt.items():
            res.append(val)
        return res



        