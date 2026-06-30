class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}
        maxLen = 0
        for num in nums:
            if num in map:
                continue
                
            beforeLen = map.get(num - 1, 0)
            afterLen = map.get(num + 1, 0)
            map[num] = beforeLen + 1 + afterLen
            map[num - beforeLen] = map[num]
            map[num + afterLen] = map[num]
            maxLen = max(maxLen, map[num])

        return maxLen



