# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Solution 1, condition flag inside recursion
        # def dfs(node):
        #     # Base case
        #     if not node:
        #         return 0, True

        #     # Recursive case
        #     lh, lh_balanced = dfs(node.left)
        #     rh, rh_balanced = dfs(node.right)

        #     if not lh_balanced or not rh_balanced:
        #         # If the tree is not balanced at any node, 
        #         # then the whole tree is considered not balanced.
        #         # Once not balanced at any node, never balanced.
        #         isBalanced = False
        #     else:
        #         # The tree was balanced uptill now, check if it continues to be balanced.
        #         isBalanced = abs(lh-rh) <= 1
            
        #     return 1 + max(lh, rh), isBalanced
        
        # _, isBalanced = dfs(root)

        # return isBalanced
        
        # Solution 2, condition flag outside recursion
        self.isBalanced = True

        def dfs(node):
            # Base case
            if not node:
                return 0

            # Recursive case
            lh = dfs(node.left)
            rh = dfs(node.right)

            # only check isBalanced if True (balanced uptill now)
            # if it is False, we keep it False, no need to check.
            if self.isBalanced and abs(lh - rh) > 1:
                self.isBalanced = False
            
            return max(lh, rh) + 1
        
        dfs(root)
        return self.isBalanced