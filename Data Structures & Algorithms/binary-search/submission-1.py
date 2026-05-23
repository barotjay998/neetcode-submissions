class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # # This is a basic binary search problem
        # # search in middle if target is greater than 
        # # look right or else look left.

        # Normal binary search.
        # L = 0
        # R = len(nums) - 1

        # while L <= R:
        #     M = L + (R - L) // 2

        #     if target > nums[M]:
        #         L = M + 1

        #     elif target < nums[M]:
        #         R = M - 1

        #     else:
        #         return M
            
        # return -1

        L, R = 0, len(nums)
        while L < R:
            M = L + (R - L) // 2
            if nums[M] >= target:
                R = M # discard the RHS, we try to reduce more and more until we find the first target occurance.
            else:
                L = M + 1
        
        return L if L < len(nums) and nums[L] == target else -1
            



        