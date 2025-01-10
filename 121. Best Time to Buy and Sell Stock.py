class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = 1000000
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > profit:
                profit = prices[i] - min_price
        return profit
