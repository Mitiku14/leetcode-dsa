class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1_freq = Counter(s1)
        s2_freq = defaultdict(int)
        l = 0

        for r in range(len(s2)):
            s2_freq[s2[r]] += 1
            while r - l + 1 >= n:
                if s1_freq == s2_freq:
                    return True
                else:

                    s2_freq[s2[l]] -= 1
                    if s2_freq[s2[l]] == 0:
                        del s2_freq[s2[l]]
                    l += 1
        return False

