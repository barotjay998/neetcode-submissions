class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # Input, we have a 2D grid, only 0, 1.
        # 0 land, 1 rock.
        # Can only move horizontally and vertically in the grid.
        # Top left, to Bottom right we need to return number of 
        # valid paths.

        # DFS, depth first search algorithm, we go in one direction
        # as far as we can and then backtrack and explore different path.

        # Get the grid dimensions
        ROWS, COLS = len(grid), len(grid[0])
        direct = [[0,1],[1,0],[0,-1],[-1,0]]
        visit = set()

        def dfs(r, c):
            # Base case
            # Check if in bounds
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == 1:
                return 0

            # Check if destination
            if r == ROWS -1 and c == COLS-1:
                return 1

            # Recursive case
            count = 0
            visit.add((r, c))

            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)
            
            # backtracking
            visit.remove((r, c))
            return count
                

        return dfs(0, 0)