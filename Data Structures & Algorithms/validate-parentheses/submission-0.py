class Solution:
    def isOpen(self, ch: str) -> bool:
        return ch in ['[', '{', '(']
    
    def getClose(self, ch: str) -> bool:
        mp = {
            '[' : ']',
            '{' : '}',
            '(' : ')'
        }
        return mp[ch]
    
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if self.isOpen(ch):
                st.append(ch)
                continue
            
            # you are at closed brack
            if st and self.getClose(st[-1]) == ch:
                st.pop()
            else:
                return False
        
        return len(st) == 0
        