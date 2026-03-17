class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        n = len(s)
        l = 0
        r = n -1
        def rev(l, r):
            if l > r:
                return []
            s[l], s[r] = s[r], s[l]
            rev(l+1, r-1)
    

        rev(l, r)
        return s
            
      