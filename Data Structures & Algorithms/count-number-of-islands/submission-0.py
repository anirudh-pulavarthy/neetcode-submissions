class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j, target, newNumber):
            # print(i, j, m, n)
            if not ((0 <= i < m) and (0 <= j < n)): return
            
            # print("I am here")
            if grid[i][j] != '1': return

            grid[i][j] = newNumber
            dfs(i + 1, j, target, newNumber)
            dfs(i - 1, j, target, newNumber)
            dfs(i, j + 1, target, newNumber)
            dfs(i, j - 1, target, newNumber)

        number = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j, grid[i][j],number)
                    number += 1

        # print(grid)
        return number - 2