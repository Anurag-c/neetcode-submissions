class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        start, ans, maxFreq = 0, 0, 0
        n = len(s)

        for end in range(n):
            seen[s[end]] += 1
            maxFreq = max(maxFreq, seen[s[end]])

            while (end - start + 1) - maxFreq > k:
                seen[s[start]] -= 1
                start += 1
            
            ans = max(ans, end - start + 1)
        
        return ans
        