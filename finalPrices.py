class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for i in range(len(prices) - 1):
            dp = prices[i]
            change = False
            for j in range(i+1, len(prices)):
                if (prices[i] - prices[j] >= 0) & (change == False):
                    change = True
                    dp = prices[i] - prices[j]
            result.append(dp)
        result.append(prices[-1])
        return result
