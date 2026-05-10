# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Each node while backtracking should always return back the 
        # maxdepth to the parent node.
        # At each node, we also need to update the diameter of the tree
        # diameter = max(diameter, maxdepth_l + maxdepth_r)
        # The longest path will always be the path between the leaf nodes or between
        # the leaf and the root node.
        self.diameter = 0

        def dfs(node):
            # Base case
            if not node:
                return 0

            # Recursive case
            depth_l = dfs(node.left)
            depth_r = dfs(node.right)
            self.diameter = max(self.diameter, depth_l + depth_r)
            return max(depth_l, depth_r) + 1
        
        maxdepth = dfs(root)
        print(f"maxdepth {maxdepth}, diameter {self.diameter}")
        return self.diameter