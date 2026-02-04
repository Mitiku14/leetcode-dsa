class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        # single_comment = False
        multi_comment = False
        temp = ""
        for s in source:
            i = 0
            # print(s)
            while i < len(s):
                if s[i:i+2] == "/*" and multi_comment == False:

                    multi_comment = True
                    i += 2
                elif s[i: i+2] == "*/" and multi_comment == True:
                    multi_comment = False
                    i += 2
                elif s[i: i+2] == "//" and multi_comment == False:
                    break

                elif  multi_comment == False:
                    temp += s[i]
                    i += 1
                else: 
                    i += 1
            if temp != "" and not multi_comment:
                ans.append(temp)
                temp = ""
        return ans
                
            
        
