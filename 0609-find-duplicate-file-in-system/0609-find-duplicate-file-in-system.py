class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        cnt = defaultdict(list)
        for ch in paths:
            parts = ch.split()
            directory = parts[0]
            files = parts[1:]
           
            for f in files:
                name, content= f.split("(")
                content = content[:-1]
                full_path = directory + "/" + name
                cnt[content].append(full_path)
        res = []
        for v in cnt.values():
      
            if len(v) > 1:
                res.append(v)
        return res

                

        
                

                
                