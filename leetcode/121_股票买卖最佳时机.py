class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        bot, best = prices[0], 0
        for i in range(len(prices)):
            bot = min(bot, prices[i])
            best = max(best, prices[i] - bot)
        return best

