class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        for price in prices:
            profit = max(profit, price - minPrice)
            minPrice = min(minPrice, price)

        return profit