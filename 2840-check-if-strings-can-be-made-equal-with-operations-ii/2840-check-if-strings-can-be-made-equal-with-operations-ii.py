class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_even = []
        s2_even = []
        s1_odd  = []
        s2_odd  = []
        for i in range(len(s1)):
            if i % 2 == 0:
                s1_even.append(s1[i])
                s2_even.append(s2[i])
            else:
                s1_odd.append(s1[i])
                s2_odd.append(s2[i])
        
        return Counter(s1_even) == Counter(s2_even) and Counter(s1_odd) == Counter(s2_odd)


