class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        ans = 0
        for i in range(n):
            curr_profit = prices[i]- min_price   # Subrtracting Intial element from the next element
            ans = max(curr_profit,ans)
            min_price = min(min_price,prices[i])  # Calculating the minimum price from the min_price(price[0], prices[i]) so that only the minimum is obtained  
        return ans