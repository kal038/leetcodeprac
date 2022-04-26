class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        actually it is pretty simple if you draw the graph,
        you only need to compound every rising edge to get the total profit
        this is possible because you can alternate between buying and selling continuously
        '''
        res = 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                res += (prices[i+1] - prices[i])
        return res
        