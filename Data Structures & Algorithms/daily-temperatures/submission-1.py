class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonically increasing stack
        result = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                val, idx = stack.pop()
                result[idx] = i - idx
            
            stack.append([temperatures[i], i])
        
        return result
        
        
        # Brute Force Approach T: O(n^2)
        # res = []

        # for i in range(len(temperatures)):
        #     found_warmer = False
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             res.append(j - i)
        #             found_warmer = True
        #             break
        #     if not found_warmer:
        #         res.append(0)
        
        # return res