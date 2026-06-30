class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tfreq = defaultdict(int)
        for ch in t:
            tfreq[ch] += 1

        sfreq = defaultdict(int)
        start, end, match = 0, 0, 0
        n, m = len(s), len(t)
        ans = ""
        while end < n:
            ch = s[end]
            sfreq[ch] += 1
            if ch in tfreq and sfreq[ch] <= tfreq[ch]:
                match += 1
            end += 1

            while match == m:
                if ans == "" or end - start < len(ans):
                    ans = s[start:end]
                    
                ch = s[start]
                if ch in tfreq and sfreq[ch] <= tfreq[ch]:
                    match -= 1
                sfreq[ch] -= 1
                start += 1
        
        return ans

        