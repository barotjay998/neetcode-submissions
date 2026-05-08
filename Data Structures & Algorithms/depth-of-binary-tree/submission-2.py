# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # We can run a DFS algorithm that explores all the paths
        # each node will add +1 to the path length and return 
        # to the parent node the length of only the longest among the two paths

        # # DFS
        # # Base case
        # if not root:
        #     return 0

        # # Recursive case
        # depth_left = self.maxDepth(root.left)
        # depth_right = self.maxDepth(root.right)
        # return 1 + max(depth_left, depth_right)

        # BFS
        q = deque()
        level = 0

        if root:
            q.append(root)

        while q:
            for _ in range(len(q)):
                # pop from the queue
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1
        
        return level
            



        
        