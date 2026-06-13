class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        mapp = [chr(97 +i) for i in range(25, -1, -1)]
        ans = []
        weight_w = {mapp[25 - i]: weights[i] for i in range(26)}

        for i in range(len(words)):
            temp = 0
            for w in words[i]:
                temp += weight_w[w]
            
            ans.append(mapp[temp % 26])
        
        return ''.join(ans)

