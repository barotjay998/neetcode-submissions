class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Nums may contain duplicates, so we sort it first 
        # so that the same numbers are next to each other, and we can skip them
        # when we need.
        # Sorting is nlogn and finding subsets is 2^n so it is ok to sort.
        curset, subsets = [], []
        nums.sort()

        def dfs(idx):
            # Base case
            if idx >= len(nums):
                subsets.append(curset.copy())
                return 

            # Recursive case
            curset.append(nums[idx])
            dfs(idx + 1)
            curset.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            dfs(idx + 1)
    
        dfs(0)
        return subsets