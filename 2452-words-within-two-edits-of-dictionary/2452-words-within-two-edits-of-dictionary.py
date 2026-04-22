class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        seen = set()
        for query in queries:
            for di in dictionary:
                
                count = 0
                for i in range(len(query)):
                    if query[i] != di[i]:
                        count += 1
                        if count > 2:
                            break
                if count <= 2:
                    res.append(query)
                    break
        
                
        return res
                

                

