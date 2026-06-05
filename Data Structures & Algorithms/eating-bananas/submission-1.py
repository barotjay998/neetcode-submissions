class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h should be min len(piles) no. of piles

        def hoursToComplete(k):
            total = 0
            for p in piles:
                t = math.ceil(p / k)
                total += t
            
            return total
        

        L = 1
        maxPile = max(piles)
        R = maxPile
        
        while L < R:
            M = L + (R - L) // 2

            if hoursToComplete(M) <= h:
                R = M
            
            else:
                L = M + 1
        
        return L if L <= maxPile else 1
        
        
        
