class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        freq = Counter(changed)
        changed.sort()
        res = []
        for num in changed:
            if freq[num] == 0:
                continue
            if freq[2 * num] == 0:
                return []
            res.append(num)
            freq[num] -= 1
            freq[2 * num]  -= 1
        return res

        
                


        
        