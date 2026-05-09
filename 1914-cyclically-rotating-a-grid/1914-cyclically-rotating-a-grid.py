class Solution:
    def rotateGrid(self, grid, k):
        m, n = len(grid), len(grid[0])

        layers = min(m, n) // 2

        for layer in range(layers):

            arr = []
            for j in range(layer, n - layer):
                arr.append(grid[layer][j])

            # right
            for i in range(layer + 1, m - layer - 1):
                arr.append(grid[i][n - layer - 1])

            # bottom
            for j in range(n - layer - 1, layer - 1, -1):
                arr.append(grid[m - layer - 1][j])

            # left
            for i in range(m - layer - 2, layer, -1):
                arr.append(grid[i][layer])

            # rotate
            k2 = k % len(arr)
            arr = arr[k2:] + arr[:k2]

            idx = 0

            # top
            for j in range(layer, n - layer):
                grid[layer][j] = arr[idx]
                idx += 1

            # right
            for i in range(layer + 1, m - layer - 1):
                grid[i][n - layer - 1] = arr[idx]
                idx += 1

            # bottom
            for j in range(n - layer - 1, layer - 1, -1):
                grid[m - layer - 1][j] = arr[idx]
                idx += 1

            # left
            for i in range(m - layer - 2, layer, -1):
                grid[i][layer] = arr[idx]
                idx += 1

        return grid