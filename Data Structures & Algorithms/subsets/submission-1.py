class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs_helper(idx, curset, subsets):
            # Base case
            if idx >= len(nums):
                subsets.append(curset.copy())
                return subsets

            # Recursive case
            curset.append(nums[idx])
            dfs_helper(idx + 1, curset, subsets)
            curset.pop()
            dfs_helper(idx + 1, curset, subsets)
            return subsets

        return dfs_helper(0, [], [])
