class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = defaultdict(int)
        for ch in s1:
            freq1[ch] += 1
        
        start, end = 0, 0
        n, m = len(s1), len(s2)
        freq2 = defaultdict(int)

        while end < m:
            ch = s2[end]
            freq2[ch] += 1
            end += 1

            while freq2[ch] > freq1[ch]:
                freq2[s2[start]] -= 1
                start += 1
            
            if end - start == n:
                return True
        
        return False



        