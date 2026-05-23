class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # This is a basic binary search problem
        # search in middle if target is greater than 
        # look right or else look left.

        '''
        Normal binary search, no support for multiple occurance of target.
        L, R points start at valid ends. 
        We return the target value if found from inside the while loop
        When the while loop ends, we know for sure the value does not exist in the array.
        '''
        # L, R = 0, len(nums) - 1
        # while L <= R:
        #     M = L + (R - L) // 2
        #     if target > nums[M]:
        #         L = M + 1
        #     elif target < nums[M]:
        #         R = M - 1
        #     else:
        #         return M
            
        # return -1

        '''
        Lower bound binary search version, handels multiple occurance of a target appearing, 
        and returns the first occurance. L starts at the first index, R at one index outside the array.
        We let the entire while loop run, target is found or not is check afterwards. 
        The idea is to 
        '''
        # L, R = 0, len(nums)
        # while L < R:
        #     M = L + (R - L) // 2
        #     if nums[M] >= target:
        #         R = M # discard the RHS, we try to reduce more and more until we find the first target occurance.
        #     else:
        #         L = M + 1
        
        # return L if L < len(nums) and nums[L] == target else -1


        '''
        Upper bound binary search version, handels multiple occurance of a target appearing and
        returns the last occurance. L starts at the first index and R at one index outside the array.
        We let the entire loop run, target is found or not is checked afterwards. 
        '''
        L, R = 0, len(nums)
        while L < R:
            M = L + (R - L) // 2
            if nums[M] > target:
                R = M 
            else:
                L = M + 1
        
        return L - 1 if L > 0 and nums[L - 1] == target else -1
            



        