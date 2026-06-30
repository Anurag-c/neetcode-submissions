class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = defaultdict(int)
        start, ans = 0, 0

        for end in range(n):
            # add character to substring
            ch = s[end]
            seen[ch] += 1

            # avoid duplicates
            while seen[ch] > 1:
                seen[s[start]] -= 1
                start += 1
            
            ans = max(ans, end - start + 1)

        return ans

        