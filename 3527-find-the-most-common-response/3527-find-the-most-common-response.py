class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        freq = defaultdict(int)
        for i in range(len(responses)):
            cnt = list(set(responses[i]))
            for v in cnt:
                freq[v] += 1
        sorted_item = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        return sorted_item[0][0]
        


            

