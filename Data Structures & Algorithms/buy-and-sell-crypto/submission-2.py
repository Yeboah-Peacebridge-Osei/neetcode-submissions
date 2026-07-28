class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        left = 0
        for right in range(len(prices)):
            #keep taking diff to store highest ever
            currentdiff = prices[right] - prices[left]
            result = max(result, currentdiff)

            #if we find a smaller buyout option, lets go get it
            if prices[left] >= prices[right]:
                left = right

        return result



        