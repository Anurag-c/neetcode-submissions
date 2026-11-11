class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        minEle = nums[low]
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= nums[high]:
                minEle = min(minEle, nums[mid])
                high = mid - 1
            else:
                low = mid + 1

        return minEle