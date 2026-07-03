class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        ans = 0

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                barIdx = stack.pop()
                nextSmallerLeft = stack[-1] if stack else -1
                area = (i - nextSmallerLeft - 1) * heights[barIdx]
                ans = max(ans, area)
            
            stack.append(i)

        while stack:
            barIdx = stack.pop()
            nextSmallerLeft = stack[-1] if stack else -1
            area = (n - nextSmallerLeft - 1) * heights[barIdx]
            ans = max(ans, area)
        
        return ans



            
        