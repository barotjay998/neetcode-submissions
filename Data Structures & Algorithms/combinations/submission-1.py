class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # T: (k * 2^n)
        curset, subsetsK = [], []

        def helper(i):
            # base case
            if len(curset) == k:
                subsetsK.append(curset.copy())
                return
            
            if i > n:
                return

            # recursive case
            curset.append(i)
            helper(i + 1)

            curset.pop()
            helper(i + 1)
        

        helper(1)
        return subsetsK
        
        # # T: (k * C(n,k))
        # curset, subsetsK = [], []

        # def dfs_helper(i):
        #     # Base case
        #     if len(curset) == k:
        #         subsetsK.append(curset.copy())
        #         return
            
        #     if i > n:
        #         return

        #     # Recursive case
        #     # Fill up poistion at this depth of recursion, 
        #     # k = depth of recursion, for k = 1 you are 
        #     # finding values for the first position, hence you go
        #     # through all the values form 1 - n as valid for first position.
        #     for j in range(i, n + 1):
        #         # You fill this position
        #         curset.append(j)

        #         # For the next position, you need all values greater than 
        #         # the first position.
        #         dfs_helper(j + 1)

        #         curset.pop()
        

        # # From [1-n] we want get all combinations of size k
        # # it is like creating subsets with size restrictions.
        # dfs_helper(1)
        # return subsetsK