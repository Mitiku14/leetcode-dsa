class Solution:
    def minimumSteps(self, s: str) -> int:
        holder = 0
        seeker = 0
        s = list(s)
        print(s)
        count = 0
        while seeker < len(s):
            if s[seeker] == '0':
                s[seeker], s[holder]  = s[holder], s[seeker]
                count += seeker - holder
                holder += 1
            seeker += 1
        return count