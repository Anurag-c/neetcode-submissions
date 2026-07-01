class Solution:
    def eval(self, a: int, b: int, op: str) -> int:
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        st = []

        for ch in tokens:
            if ch not in ops:
                st.append(int(ch))
            else:
                b, a = st.pop(), st.pop()
                st.append(self.eval(a, b, ch))
        
        return st[0]
        