class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, len(prices) - 1
        buyPrice, sellPrice = prices[0], prices[len(prices) - 1]
        while(l < r):
            print('l:', l, 'r:', r, 'buyPrice:', buyPrice, 'sellPrice:', sellPrice, 'prices:', prices[l], prices[r])
            if(buyPrice > sellPrice):
                l +=1
                buyPrice = min(buyPrice, prices[l])
            else:
                r -=1
                sellPrice = max(sellPrice, prices[r])
        return sellPrice - buyPrice


