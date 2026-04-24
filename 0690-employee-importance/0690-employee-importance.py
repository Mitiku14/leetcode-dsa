"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapp = defaultdict(list)
        imp = {}

        for i in range(len(employees)):
            emp = employees[i]

            imp[emp.id] = emp.importance
            for sub in emp.subordinates:
                mapp[emp.id].append(sub)
        tot = 0
        q = deque([id])
        while q:
            node = q.popleft()
            tot += imp[node]
            for ng in mapp[node]:
                q.append(ng)
        return tot




        
        



        

    
        
