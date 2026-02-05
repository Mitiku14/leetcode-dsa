class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_dict = defaultdict(set)
        # guess_dict = {}
        count_bulls = count_cows = 0
        res = []
        for index, char in enumerate(secret):
            secret_dict[char].add(index)
        
        for index, item  in enumerate(guess):
            if item in secret_dict:
                if index in secret_dict[item]:
                    count_bulls += 1
                    secret_dict[item].remove(index)
                
                else:
                    res.append(item)
        for it in res:
            if secret_dict[it]:
                secret_dict[it].pop()
                count_cows += 1
            
            


            
        return (str(count_bulls) + "A" + str(count_cows) + "B")