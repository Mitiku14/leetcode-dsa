class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        seen = set()
        res = ""
        seen.add("")
        for word in words:
            if word[:-1] in seen:
                if len(word) > len(res):
                    res = word
                seen.add(word)
        
        return res



        
        