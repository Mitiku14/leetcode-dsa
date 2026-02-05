class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_dict = defaultdict(int)
        for index , lst in enumerate(list1):
            list1_dict[lst] = index
        res = []
        min_ind = float('inf')
      
        for index , lst in enumerate(list2):
            if lst in list1_dict:
                if list1_dict[lst] + index <= min_ind:
                    min_ind = min(min_ind, (list1_dict[lst] + index))

        for k, v in enumerate(list2):
            if v in list1_dict and list1_dict[v] + k == min_ind:
                res.append(v)

        return res
