class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        charToW = {}
        wordToC = {}
        for ch, word in zip(pattern, words):
            if ch in charToW:
                if charToW[ch] != word:
                    return False
            else:
                charToW[ch] = word
            
            if word in wordToC:
                if wordToC[word] != ch:
                    return False
            else:
                wordToC[word] = ch
        
        return True