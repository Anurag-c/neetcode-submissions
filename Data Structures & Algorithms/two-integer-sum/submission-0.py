class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            j = seen.get(target - nums[i])
            if j != None:
                return [j, i]
                
            seen[nums[i]] = i
        
        return [-1, -1]
        