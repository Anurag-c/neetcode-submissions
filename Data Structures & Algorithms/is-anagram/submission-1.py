class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLen, tLen = len(s), len(t)
        if sLen != tLen:
            return False
        
        countS, countT = {}, {}
        for i in range(sLen):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT