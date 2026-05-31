class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        cur = mass
        for am in asteroids:
            if am > cur:
                return False
            cur += am
        
        return True
