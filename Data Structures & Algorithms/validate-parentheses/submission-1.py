class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        openToClose = {
            '[' : ']',
            '{' : '}',
            '(' : ')'
        }

        for ch in s:
            if ch in openToClose:
                st.append(ch)
                continue
            
            # you are at closed brack
            if st and openToClose[st[-1]] == ch:
                st.pop()
            else:
                return False
        
        return len(st) == 0
        