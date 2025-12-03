class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        for word in range(1, len(words)):
            if Counter(words[word]) != Counter(res[-1]):
                res.append(words[word])
        return res
            


            