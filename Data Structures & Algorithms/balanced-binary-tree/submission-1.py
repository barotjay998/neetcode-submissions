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
            lh, lh_balanced = dfs(node.left)
            rh, rh_balanced = dfs(node.right)

            if not lh_balanced or not rh_balanced:
                # If the tree is not balanced at any node, 
                # then the whole tree is considered not balanced.
                # Once not balanced at any node, never balanced.
                isBalanced = False
            else:
                # The tree was balanced uptill now, check if it continues to be balanced.
                isBalanced = abs(lh-rh) <= 1
            
            return 1 + max(lh, rh), isBalanced
        
        _, isBalanced = dfs(root)

        return isBalanced