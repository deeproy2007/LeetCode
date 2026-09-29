class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        
        # 1. Initialize the top-left cell (Base Case)
        # grid[0][0] is already correct
        
        # 2. Fill the first row (can only move right)
        for j in range(1, cols):
            grid[0][j] += grid[0][j - 1]
            
        # 3. Fill the first column (can only move down)
        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]
            
        # 4. Fill the rest of the inner grid
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                
        # The target cell holds the final minimized sum
        return grid[rows - 1][cols - 1]
