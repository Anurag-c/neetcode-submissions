class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0 for _ in temperatures]

        for (i, val) in enumerate(temperatures):
            while st and val > temperatures[st[-1]]:
                res[st[-1]] = i - st[-1]
                st.pop()
            
            st.append(i)
        
        return res