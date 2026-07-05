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
        ROWS, COLS = len(grid), len(grid[0])
        direct = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = deque()
        visit = set()

        # init for BFS
        q.append((0, 0))
        visit.add((0, 0))

        level = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                # Check if this is the destination
                if r == ROWS - 1 and c == COLS - 1:
                    return level
                
                # Add the next level valid nodes to the queue & visit.
                for dr, dc in direct:
                    nr, nc = dr + r, dc + c

                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visit or grid[nr][nc] == 1:
                        continue

                    q.append((nr, nc))
                    visit.add((nr, nc))
            

            level += 1 

        return -1


            

