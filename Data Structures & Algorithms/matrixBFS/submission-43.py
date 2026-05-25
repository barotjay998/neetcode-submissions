class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # Shortest path algorithm (BFS) is the most effecient
        # way to find the shortest path from src to dst node
        # in a non weighted graph network. Currently we have a
        # matrix grid based network, the network can be of other 
        # forms such as linked nodes, adjacency list.
        # T: O(M*N) - each node is processed only once and hence effecient, no backtracking involved.
        # BFS uses queues and visit hashset data strucutes
        # Concept is of Adding the nodes and Getting the nodes from the queue, 
        # once a node is popped from the queue it is never ever addedto the queue
        # again, we make sure of this using the visit hashset.

        # Setup
        # Getting the grid dimensions, in any of the grid 
        # problem this is the first step.
        # ROWS, COLS = len(grid), len(grid[0])
        
        # q = collections.deque()
        # visit = set()
        # direct = [[0, 1],[0, -1],[1, 0],[-1, 0]]
        # level = 0

        # # Add the src node to the queue as init to BFS
        # q.append((0, 0))
        # visit.add((0, 0))

        # while q:
        #     for _ in range(len(q)):
        #         r, c = q.popleft()

        #         # If dst node return the current level = shortest path
        #         if r == ROWS - 1 and c == COLS - 1:
        #             return level
                
        #         # Not not the dst node then add all the valid neighbours (part of next level)
        #         for dr, dc in direct:
        #             nr, nc = dr + r, dc + c

        #             if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 1 or (nr, nc) in visit:
        #                 continue
                    
        #             q.append((nr, nc))
        #             visit.add((nr, nc))

        #     level += 1
        
        # # No path possible
        # return -1


        ROWS, COLS = len(grid), len(grid[0])

        q = collections.deque()
        visit = set()
        direct = [[0,1],[0,-1],[1,0],[-1,0]]

        q.append((0, 0))
        visit.add((0, 0))
        level = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return level
                
                for dr, dc in direct:
                    nr, nc = dr + r, dc + c
                    
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 1 or (nr, nc) in visit:
                        continue
                    
                    q.append((nr, nc))
                    visit.add((nr, nc))
            
            level += 1
        
        return -1

            

