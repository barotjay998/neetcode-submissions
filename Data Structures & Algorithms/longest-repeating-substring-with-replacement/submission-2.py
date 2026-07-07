class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # L, R = 0, 0
        # res = 0
        # countInWindow = [0] * 26

        # while R < len(s):
        #     if (R - L + 1) - max(countInWindow) <= k:
        #         countInWindow[ord(s[R]) - ord('A')] += 1
        #         res = max(res, R - L + 1)
        #         R += 1

        #     else:
        #         countInWindow[ord(s[L]) - ord('A')] -= 1
        #         L += 1
        
        # return res

        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res