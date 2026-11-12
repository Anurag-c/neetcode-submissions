class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)

        total = len1 + len2
        isEven = (total % 2 == 0)
        half = total // 2
        low, high = 0, len1
        
        while low <= high:
            numLeftFrom1 = (low + high) // 2
            numLeftFrom2 = half - numLeftFrom1

            leftEle1 = nums1[numLeftFrom1 - 1] if numLeftFrom1 - 1 >= 0 else -math.inf
            leftEle2 = nums2[numLeftFrom2 - 1] if numLeftFrom2 - 1 >= 0 else -math.inf
            rightEle1 = nums1[numLeftFrom1] if numLeftFrom1 < len1 else math.inf
            rightEle2 = nums2[numLeftFrom2] if numLeftFrom2 < len2 else math.inf

            maxLeft = max(leftEle1, leftEle2)
            minRight = min(rightEle1, rightEle2)

            if maxLeft <= minRight:
                if isEven:
                    return (maxLeft + minRight) / 2.0
                return minRight

            if leftEle1 > rightEle2:
                high = numLeftFrom1 - 1
            else:
                low = numLeftFrom1 + 1
        
        return -1

            
