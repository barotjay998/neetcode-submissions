class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # This is a basic binary search problem
        # search in middle if target is greater than 
        # look right or else look left.

        L = 0
        R = len(nums) - 1

        while L <= R:
            M = L + (R - L) // 2

            if target > nums[M]:
                L = M + 1

            elif target < nums[M]:
                R = M - 1

            else:
                return M
            
        return -1

        