class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefixProd = 1
        for num in nums:
            ans.append(prefixProd)
            prefixProd *= num

        suffixProd = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * suffixProd
            suffixProd *= nums[i]
        
        return ans

        