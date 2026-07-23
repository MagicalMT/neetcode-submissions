class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = 0
        for i in range(1, len(prices)):
            if min(prices[:i]) < prices[i]:
                diff = prices[i] - min(prices[:i])
                if price < diff:
                    price = diff
        return price