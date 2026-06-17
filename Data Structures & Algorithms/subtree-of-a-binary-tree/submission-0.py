# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def cloneCheck(sr1, sr2):
            # Returns: True if they are clone, False if they are not.
            # Base cases:
            # Both are NULL, we're good.
            if not sr1 and not sr2:
                return True
            
            # One of the nodes NULL, not a clone.
            if (not sr1 and sr2) or (sr1 and not sr2):
                return False

            # Recursive case:
            if sr1.val != sr2.val:
                return False
            
            leftSub = cloneCheck(sr1.left, sr2.left)
            rightSub = cloneCheck(sr1.right, sr2.right)

            return leftSub and rightSub
        

        def dfs_helper(node, subRoot):
            # Base cases
            if not node:
                return False

            # Recursive cases
            if node.val == subRoot.val:
                if cloneCheck(node, subRoot):
                    return True 
            
            if dfs_helper(node.left, subRoot):
                return True

            if dfs_helper(node.right, subRoot):
                return True
            
            return False
        
        return dfs_helper(root, subRoot)
            