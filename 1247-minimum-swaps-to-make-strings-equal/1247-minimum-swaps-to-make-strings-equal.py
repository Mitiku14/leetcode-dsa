class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        cnt_s1 = Counter(s1)
        cnt_s2 = Counter(s2)
        if (cnt_s1["x"] + cnt_s2["x"]) % 2  or  (cnt_s1["y"] + cnt_s2["y"]) % 2:
            return -1
        
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        for i in range(len(s1)):
            if s1[i] !=  s2[i]:
                cnt1[s1[i]] += 1
                cnt2[s2[i]] += 1
        

        val = (cnt1['x'] + cnt1['y']) // 2
        if "x" not in cnt1 or "y" not in cnt1:
            return val
        
        return val + min(cnt1["x"],cnt1["y"])
        
        
        