class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # # Brute force solution T:O(n^2)
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        #             break

        # cache = {}
        # for i in range(len(numbers)):
        #     if target - numbers[i] in cache:
        #         return [cache[target-numbers[i]] + 1, i + 1]
            
        #     cache[numbers[i]] = i
        

        # Two Pointers T: O(n), No extra space
        # The input array is already sorted.
        L, R = 0, len(numbers) - 1
        while L < R:
            if numbers[L] + numbers[R] > target:
                R -= 1
            elif numbers[L] + numbers[R] < target:
                L += 1
            else:
                return [L + 1, R + 1]
        