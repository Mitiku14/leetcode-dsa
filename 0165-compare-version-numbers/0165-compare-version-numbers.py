class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        x = version1.split(".")
        y = version2.split(".")
        cnt1 = cnt2 = 0
        for x1 , y1 in zip(x, y):
            print(x1, y1)
            if int(x1) < int(y1):
                cnt2 += 1
            elif int(x1) > int(y1):
                cnt1 += 1
        if cnt1 > cnt2:
            return 1
        elif cnt1 < cnt2:
            return -1
        else:
            return 0



    
