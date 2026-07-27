class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        for idx in range(len(prices)-1):
            for jdx in range(idx+1, len(prices)):
                diff = prices[jdx] - prices[idx]
                result = max(result, diff)

        return result
        