# Last updated: 15/9/2026, 11:35:43 pm
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]

        for price in prices[1:]:
            prev_cash = cash
            
            cash = max(cash, hold + price - fee)
            hold = max(hold, prev_cash - price)

        return cash