class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
        print(perms)
        return perms



        # # In case of permutations we build the result from the base case

        # Recursive Alogrithm
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

        # # Iterative Algorithm 
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
            


