class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        dct = [(-1,-1), (-1,0), (-1,1), 
            ( 0,-1), ( 0,0), ( 0,1), 
            ( 1,-1), ( 1,0), ( 1,1)]

        smoother = [[0] * col for _ in range(row)]
        for i in range(row):
            total = 0
            count = 0
            for j in range(col):
                for nr, nc in dct:
                    new_r = i + nr
                    new_c = j + nc
                    if 0 <= new_r <  row and 0 <= new_c < col:
                        total += img[new_r][new_c]
                        count += 1
                temp = total // count
                smoother[i][j] = temp
                total = 0
                count = 0
        return smoother


                    

                

