class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1, n + 1))
        ind = 0
        while len(players) > 1:
            ind = (ind + k - 1) % len(players)
            players.pop(ind)
        
        return players[0]