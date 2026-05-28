# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Traverse the two trees at the same time 
        # DFS or BFS algorithm and compare the nodes 

        def dfs(treeNodep, treeNodeq):
            # Base case
            # If both the nodes are None, then we are good
            # the trees are still the same
            if treeNodep == None and treeNodeq == None:
                return True
             
            # If one of the tree nodes is None and other is not,
            # then the trees are different.
            elif (treeNodep and treeNodeq == None) or (treeNodep == None and treeNodeq):
                return False

            # Recursive case
            # Both nodes are not None, so we check their value first
            # If they are not the same no point of checking further.
            if treeNodep.val != treeNodeq.val:
                return False

            # Nodes have same value, so now we check their left and right childrens
            left_child = dfs(treeNodep.left, treeNodeq.left)
            right_child = dfs(treeNodep.right, treeNodeq.right)

            return left_child and right_child
             

        return dfs(p, q)