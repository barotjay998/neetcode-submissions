"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        newGraph = {}

        q = deque()
        visit = set()
        q.append(node)
        visit.add(node)
       
        newGraph[node.val] = Node(val=node.val)

        while q:
            n = q.popleft()
            
            # Process neighbours
            for neighbors in n.neighbors:
                if neighbors not in visit:
                    q.append(neighbors)
                    visit.add(neighbors)

                # Check if neighbours exist in newGraph
                if neighbors.val not in newGraph:
                    newGraph[neighbors.val] = Node(val=neighbors.val)

                newGraph[n.val].neighbors.append(newGraph[neighbors.val])
        
        return newGraph[node.val]







