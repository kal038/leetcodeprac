class Solution(object):
    def myPow(self, x, n):
        '''
        O(n) solution just don't work
        O(logn) solution: Divide and conquer
        
        '''
        
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            
            res = helper(x, n//2)
            res = res * res
            return (x*res) if n % 2 else res
        
        res = helper(x, abs(n))
        return res if n >= 0 else 1/res
        # t=abs(n)
        # ans=1
        # while(t>0):
        #     if(t%2==0):
        #         x=x*x
        #         t=t//2
        #     else:
        #         ans=ans*x
        #         t=t-1
        # if(n<0):
        #     return 1/ans
        # else:
        #     return ans
        
     