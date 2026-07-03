class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(float('-inf'))
        n = len(heights)
        stack = []
        ans = 0

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                barIdx = stack.pop()
                nextSmallerLeft = stack[-1] if stack else -1
                area = (i - nextSmallerLeft - 1) * heights[barIdx]
                ans = max(ans, area)
            
            stack.append(i)
        
        return ans



            
        