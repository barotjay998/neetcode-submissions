class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # T: O(k * C(n, k)) combination technique 2 - fill up positions.
        curset, subsetsK, cursum = [], [], 0
        self.cursum = 0

        def helper(idx):
            # Base case
            if self.cursum == target:
                subsetsK.append(curset.copy())
                return
            
            if self.cursum > target:
                return
            
            if idx >= len(nums):
                return 
            
            # Recursive case
            for jdx in range(idx, len(nums)):
                curset.append(nums[jdx])
                self.cursum += nums[jdx]
                helper(jdx)
                self.cursum -= nums[jdx]
                curset.pop()
        
        helper(0)
        return subsetsK
            
            