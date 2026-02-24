class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        l, r = 0, n - 1
        target_sum = skill[l] + skill[r]
        prod = 0
        while l  <= r :
            if skill[l] + skill[r] == target_sum:
                pr = skill[l] * skill[r]
                prod += pr
                l += 1
                r -= 1
            else:
                return -1
            
        return prod 

        