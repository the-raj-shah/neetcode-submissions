class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        buyPrice, sellPrice = prices[0], prices[r]
        while(l < r) and r < len(prices):
            # print('l:', l, 'r:', r, 'buyPrice:', buyPrice, 'sellPrice:', sellPrice, 'prices:', prices[l], prices[r])
            if(buyPrice > sellPrice):
                buyPrice = min(buyPrice, prices[l])
                l +=1
                r +=1
            else:
                sellPrice = max(sellPrice, prices[r])
                r +=1
        return sellPrice - buyPrice


