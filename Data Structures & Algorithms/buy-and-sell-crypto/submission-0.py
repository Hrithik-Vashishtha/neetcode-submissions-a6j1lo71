class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy = 0, prices[0]
        for price in prices:
            profit = max(profit, price-buy)
            buy = min(buy, price)

        return profit