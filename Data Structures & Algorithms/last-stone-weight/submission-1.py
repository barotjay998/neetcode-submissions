class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # At eatch setp we want to find 2 heaviest stones in 
        # the array. 

        for i in range(len(stones)):
            stones[i] = stones[i] * -1

        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones) # heavy or equal
            x = heapq.heappop(stones)
            if x == y:
                continue

            else:
                heapq.heappush(stones, y - x)
        
        return 0 if not len(stones) else -1 * stones[-1]
        



