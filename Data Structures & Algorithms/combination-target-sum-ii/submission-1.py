class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # List of groups that result in target sum.
        # start creating subsets like we noramlly do,
        # at every index we have 2 choices, whether to inlucde that 
        # number in the subset or do not include that number in the subset.

        curset, result = [], []
        candidates.sort()

        def helper(idx, sum):
            # Base cases
            if sum == target:
                result.append(curset[:])
                return

            if sum > target or idx >= len(candidates):
                return

            # Recursive cases
            curset.append(candidates[idx])
            sum += candidates[idx]
            helper(idx + 1, sum)

            curset.pop()
            sum -= candidates[idx]
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1

            helper(idx + 1, sum)
        
        helper(0, 0)

        return result
