class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        maxprofit = 0
        minPurchase = prices[0]
        for i in range(1,len(prices)):
            maxprofit = max(maxprofit, prices[i] - minPurchase)
            minPurchase = min(minPurchase,prices[i])
        return maxprofit