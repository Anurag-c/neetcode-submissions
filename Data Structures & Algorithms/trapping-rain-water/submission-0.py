class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = 0, 0
        l, r = 0, len(height) - 1
        res = 0

        while l <= r:
            if maxLeft < maxRight:
                maxLeft = max(height[l], maxLeft)
                res += maxLeft - height[l]
                l += 1
            else:
                maxRight = max(height[r], maxRight)
                res += maxRight - height[r]
                r -= 1
        
        return res


        