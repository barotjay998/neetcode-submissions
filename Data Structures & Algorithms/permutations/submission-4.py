class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Method 1: Position filling logic like Combination Technique 2 in your LC notes.
        curperms, perms = [], []
        visit = set()

        def dfs_helper(idx):
            # Base case
            if len(curperms) == len(nums):
                perms.append(curperms.copy())
                return

            # Recursive case
            for i in range(len(nums)):
                if i not in visit:
                    curperms.append(nums[i])
                    visit.add(i)
                    dfs_helper(idx + 1)
                    visit.remove(i)
                    curperms.pop()

        dfs_helper(0)
        return perms

        # Method 2: Build permutations for an array from base case i.e empty array 
        # like you would do by hand. Example, for nums = [1,2] you will 
        # Step 1: start with [],
        # Step 2: then add [1], then 2 on both sides [1,2] & [2,1] - stop since length reached.
        # if you had nums = [1,2,3] you would add 
        # Step 3: adding 3 in all positions of [1,2] & [2,1]

        # # Method 2.1: Recursive Alogrithm
        # def dfs_helper(index):
        #     # Base case
        #     if index >= len(nums):
        #         return [[]]

        #     # Recursive case
        #     perms = dfs_helper(index + 1)
        #     curr_perms = []

        #     for p in perms:
        #         for j in range(len(p) + 1):
        #             p.insert(j, nums[index])
        #             curr_perms.append(p[:])
        #             p.pop(j)
            
        #     return curr_perms
        
        # return dfs_helper(0)

        # # Method 2.2: Iterative Algorithm, same logic as above recursive.
        # base_perms = [[]] # Base permutation is an empty list
        # for i in range(len(nums)):
        #     next_perms = []

        #     for p in base_perms:
        #         for j in range(len(p) + 1):
        #             p.insert(j, nums[i])
        #             next_perms.append(p[:])
        #             p.pop(j)

        #     # Update base perms
        #     base_perms = next_perms
        
        # return base_perms
            


