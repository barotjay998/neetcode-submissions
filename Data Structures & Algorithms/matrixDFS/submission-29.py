class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visit = set()

        def dfs_helper(r, c):
            # Base case
            # Node outside the grid
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == 1:
                return 0

            # Node is the destination
            if r == ROWS - 1 and c == COLS -1:
                return 1

            # Recursive case
            count = 0
            visit.add((r, c))
            for dr, dc in direct:
                count += dfs_helper(dr + r, dc + c)
            
            visit.remove((r, c))
            return count
        
        return dfs_helper(0, 0)
