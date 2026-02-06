class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = defaultdict(int)
        res = []
        for web in cpdomains:
            ct, domain = web.split()
            ct = int(ct)
            cnt[domain] += ct
            for i in range(len(domain)):

                if domain[i] == '.':
                    cnt[domain[i+1:]] += ct
        for key , val in cnt.items():
            res.append(f"{val} {key}")
        return res
        
            
        






            
        
        