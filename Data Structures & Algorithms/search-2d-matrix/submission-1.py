class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # First intiution solution, go through each row to 
        # # find the row in which target can exist, then run binary search in that row.
        # # This runs Log(N) times
        # def binarySearch(row, target):
        #     L, R = 0, len(row)

        #     while L < R:
        #         M = L + (R - L) // 2
        #         if row[M] < target:
        #             L = M + 1
        #         else:
        #             R = M
   
        #     return True if L < len(row) and row[L] == target else False

        # # This runs O(M) times
        # for row in matrix:
        #     if target >= row[0] and target <= row[-1]:
        #         return binarySearch(row, target) 
        #     # else we just skip this row
        
        # return False
        # # Total solution O(M * log(N))

        # Run binary serach on a row O(log(N))
        def binarySearch(row, target):
            L, R = 0, len(row)

            while L < R:
                M = L + (R - L) // 2
                if row[M] < target:
                    L = M + 1
                else:
                    R = M
            
            return True if L < len(row) and row[L] == target else False

        
        # Run binary search on the matrix O(log(M))
        Lrow, Rrow = 0, len(matrix)
        while Lrow < Rrow:
            Mrow = Lrow + (Rrow - Lrow) // 2
            if matrix[Mrow][0] < target and matrix[Mrow][-1] < target:
                Lrow = Mrow + 1
            
            else:
                Rrow = Mrow
        
        # Check if the row we found is inbounds and has the target
        if Lrow < len(matrix) and target >= matrix[Lrow][0] and target <= matrix[Lrow][-1]:
            # Run binary search again to check if target exist in the row
            return binarySearch(matrix[Lrow], target)
        
        return False

        # Total solution = O(log(M) + log(N)) = O(log(M * N))
                

