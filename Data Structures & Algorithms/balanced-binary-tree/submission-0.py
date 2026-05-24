# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            # Base case
            if not node:
                return 0, True

            # Recursive case
            lh, lhv = dfs(node.left)
            rh, rhv = dfs(node.right)

            if not lhv or not rhv:
                valid = False
            else:
                valid = abs(lh-rh) <= 1
            
            return 1 + max(lh, rh), valid
        
        _, valid = dfs(root)
        return valid