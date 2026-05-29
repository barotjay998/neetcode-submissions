class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subSets, curSet = [], []

        def dfs_helper(i, curSet, subSets):
            # Base case
            if i >= len(nums):
                subSets.append(curSet.copy())
                return
            
            # Recursive case
            # We choose to add ith number
            curSet.append(nums[i])
            dfs_helper(i + 1, curSet, subSets)
            curSet.pop()

            # We do not choose to add the ith number
            dfs_helper(i + 1, curSet, subSets)
        
        dfs_helper(0, curSet, subSets)
        return subSets
