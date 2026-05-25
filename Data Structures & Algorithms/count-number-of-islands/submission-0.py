class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        numIslands = 0
        q = collections.deque()
        visit = set()
        

        def bfs():
            direct = [[0, 1],[1, 0],[0, -1],[-1, 0]]
            while q:
                r, c = q.popleft()

                for dr, dc in direct:
                    nr, nc = dr + r, dc + c

                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visit or grid[nr][nc] == "0":
                        continue
                    
                    q.append((nr, nc))
                    visit.add((nr, nc))

        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit:
                    if grid[r][c] == "0":
                        visit.add((r, c))

                    else:
                        numIslands += 1
                        q.append((r, c))
                        visit.add((r, c))
                        bfs()
        
        return numIslands