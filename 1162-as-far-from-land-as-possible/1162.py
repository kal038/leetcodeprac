class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        start from land as a source, BFS until reach the last water -> that water the farthest

        Algo:
        1. Write helper function to get neighbors
        2. set up BFS by enqueing the source(s) which in this case is land
        3. BFS Spread
        """

        print(max(grid))

        if max(max(grid)) == 0 or min(min(grid)) == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def get_neighbour_water(row, col):
            water = []
            for dr, dc in dirs:
                nr, nc = dr + row, dc + col
                if (0 <= nr < ROWS and 0 <= nc < COLS) and grid[nr][nc] == 0:
                    water.append((nr, nc))

            return water

        queue = collections.deque()
        visited = set()
        distance = -1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))

        while queue:
            distance += 1

            for _ in range(len(queue)):
                row, col = queue.popleft()
                for nr, nc in get_neighbour_water(row, col):
                    if (nr, nc) in visited:
                        continue
                    else:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        return distance

