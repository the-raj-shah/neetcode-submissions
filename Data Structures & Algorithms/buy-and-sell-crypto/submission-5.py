class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l,r = 0, 1
        buyPrice, sellPrice = prices[0], prices[r]
        while(l < r) and r < len(prices):
            print('l:', l, 'r:', r, 'buyPrice:', buyPrice, 'sellPrice:', sellPrice, 'prices:', prices[l], prices[r])
            buyPrice = min(buyPrice, prices[l])
            sellPrice = max(sellPrice, prices[r])
            if(buyPrice > sellPrice):
                l +=1
                r +=1
            else:
                r +=1
        return max(sellPrice - buyPrice, 0)


