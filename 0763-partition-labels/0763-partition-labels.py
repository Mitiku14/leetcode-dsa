class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if s[0] == s[len(s) -1]:
            return [len(s)]
        last_occurrence = {char: i for i, char in enumerate(s)}
        res = []
        end = start = 0
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res

        

            
            
            