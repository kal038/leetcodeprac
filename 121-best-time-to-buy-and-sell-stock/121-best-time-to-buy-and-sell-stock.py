class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        brute force solution you compare pairs of values and take the latter value subtract the earlier value to get 
        the profit (since you can only sell AFTER you bought in)
        '''
        # res = 0
        # for i in range(len(prices) - 1):
        #     for j in range(i, len(prices)):
        #         res = max(res, prices[j] - prices[i])
        # return res
        '''
        optimized code:
        2 pointers: since our intuition tells us that we need to buy the dip, once we find a "dip", which is 
        a value that is lower than the previous one, we continuously probe to the right to calculate the profits
        and keep a running max. If we find another lower dip though, we need to probe right form that point on 
        Pseudocode:
        if len(prices) is 1 return no profit
        l = 0
        r = 1
        res = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                res = max(res, prices[r] - prices[i])
                r += 1
        return res
        
        '''
        
        if len(prices) <= 1:
            return 0
        else:
            l = 0
            r = 1
            res = 0
            while r < len(prices):
                if prices[r] < prices[l]:
                    l = r
                    r = l + 1
                else:
                    res = max(res, prices[r] - prices[l])
                    r += 1
            return res