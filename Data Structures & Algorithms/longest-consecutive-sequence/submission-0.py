class Solution:
    def lenSeq(self, start, seen):
        len = 0
        while start in seen:
            start += 1
            len += 1

        return len

    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxLen = 0
        for num in nums:
            if num - 1 not in seen:
                maxLen = max(maxLen, self.lenSeq(num, seen))

        return maxLen