class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # We will go through the full grid one by one, whenever we find an island,
        # we will do a full BFS of the entire island counting the number of cells 
        # in each island and then update the maxArea.

        self.maxArea = 0

        ROWS, COLS = len(grid), len(grid[0])
        direct = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        visit = set()
        q = collections.deque()

        def bfs():
            area = 0
            while q:
                r, c = q.popleft()
                area += 1

                for dr, dc in direct:
                    nr, nc = dr + r, dc + c

                    # We check neighbours and add only land to the queue
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visit or grid[nr][nc] == 0:
                        continue
                    
                    q.append((nr, nc))
                    visit.add((nr, nc))
            
            self.maxArea = max(self.maxArea, area)

        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit:
                    if grid[r][c] == 1:
                        q.append((r, c))
                        visit.add((r, c))
                        bfs()
                    else:
                        visit.add((r, c))
        
        return self.maxArea
                

