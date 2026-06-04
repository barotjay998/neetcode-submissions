class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # We need the signal to reach all the nodes
        # if it is not possible then we return -1 
        # if it is possible then we return the max of the shortest time to all nodes

        # First create adj list mapping nodes -> neighbouring nodes and time, fromt
        # the times list, which is simply a list of edges.
        # adjList = {}
        # for i in range(1, n + 1):
        #     adjList[i] = []
        
        # Or we can use default dict
        adjList = collections.defaultdict(list)

        for u, v, w in times:
            adjList[u].append((v, w))
        
        shortest = {}
        minheap = []
        heapq.heappush(minheap, (0, k))
        maxdist = 0

        while minheap:
            dist, node = heapq.heappop(minheap)

            if node in shortest:
                continue

            shortest[node] = dist
            maxdist = max(maxdist, dist)
            
            for neighbour in adjList[node]:
                if neighbour not in shortest:
                    heapq.heappush(minheap, (neighbour[1] + dist, neighbour[0]))
        
        if len(shortest) != n:
            return -1

        else:
            return maxdist
