class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        
        return res

    def decode(self, s: str) -> List[str]:
        words = []
        idx = 0
        n = len(s)

        while idx < n:
            # 1. extract word length
            wordLen = 0
            while s[idx] != '#':
                wordLen = (wordLen * 10) + int(s[idx])
                idx += 1
            
            # 2. extract the word
            # eg: 5#abcde
            # idx = 1, start = 2
            # wordLen = 5, end = 7
            start = idx + 1
            end = start + wordLen
            words.append(s[start:end])
            idx = end
        
        return words
            

            

