class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        par = {}
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra != rb:
                par[rb] = ra
        
        email_to_name = {}
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                if email not in par:
                    par[email] = email
                email_to_name[email] = name
        
        for acc in accounts:
            firs_email = acc[1]
            for email in acc[2:]:
                union(firs_email, email)
        
        groups = defaultdict(list)
        for email in par:
            root = find(email)
            groups[root].append(email)
        
        res = []
        for root , emails in groups.items():
            name = email_to_name[root]
            res.append(
                [name] + sorted(emails)
            )
        return res





