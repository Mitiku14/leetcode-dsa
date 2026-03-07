class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return 0
        st = s.split()
        return len(st)