grid = [["1","0","1","1","0","1","1"]]

class Solution:
    def numIslands(self, grid) -> int:
        def dfs(grid, location):
            grid[location[0]][location[1]] = "0"
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for direction in directions:
                new_location = (location[0] + direction[0], location[1] + direction[1])
                try:
                    if new_location[0] >= 0 and new_location[1] >= 0 and grid[new_location[0]][new_location[1]] == "1":
                        dfs(grid, new_location)
                except:
                    pass
        
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, (i, j))
                    counter += 1
        return counter

print(Solution().numIslands(grid))