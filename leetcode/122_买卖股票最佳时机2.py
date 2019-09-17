class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1: return 0
        bot,res=prices[0],0
        for i in range(len(prices)):
            if prices[i]<bot: bot=prices[i]
            if prices[i]>bot:
                res+=prices[i]-bot
                bot=prices[i]
        return res