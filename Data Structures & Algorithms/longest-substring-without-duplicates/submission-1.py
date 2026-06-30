class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        start, ans = 0, 0

        for end in range(n):
            # avoid duplicates
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
                
            seen.add(s[end])
            ans = max(ans, end - start + 1)

        return ans

        