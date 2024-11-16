class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        #dfs setup
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        closed_islands = 0


        #dfs helper function
        def dfs(row, col):
            # hit border
            if row < 0 or col < 0 or row == ROWS or col == COLS:
                return 0
            # visited land or hitting water
            elif grid[row][col] == 1 or (row,col) in visited:
                return 1
            # unvisited land, process and diveeee
            else:
                visited.add((row,col))
                return (dfs(row+1,col) * dfs(row-1,col) * dfs(row,col+1) * dfs(row, col-1))

        #traverse the matrix and deciding where to dive
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 and (r,c) not in visited:
                    closed_islands += dfs(r,c)

        return closed_islands

        


        
