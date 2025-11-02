class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        i, n = 0, len(s)
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break
            j = i + 1
            while j < n and s[j] != ' ':
                j += 1
            word = s[i:j]
            if res == "":
                res = word
            else:
                res = word + " " + res
            i = j + 1
        return res
        






    


