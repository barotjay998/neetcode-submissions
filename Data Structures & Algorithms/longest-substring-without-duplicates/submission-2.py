class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Edge case
        if len(s) < 2:
            return len(s)

        L, R = 0, 0 
        hashSet = set()
        result = 0

        while R < len(s):
            if s[R] in hashSet:
                result = max(result, len(hashSet))
                while s[R] in hashSet:
                    hashSet.remove(s[L])
                    L += 1

            hashSet.add(s[R])
            R += 1
        
        return max(result, len(hashSet))


        
