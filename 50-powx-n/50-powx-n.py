class Solution(object):
    def myPow(self, x, n):
        '''
        O(n) solution just don't work
        O(logn) solution: Divide and conquer
        Idea: when we have something like 2*10 we could split it down to 2**5 * 2**5 so that we only have to compute one half of it
        At 2**5, we can break it down to 2**2 * 2**2 but then that is only 2**4 so we need to multiply by x
        Pseudocode:
            base case n = 0 return 1
            x = 0 return 0
            
            recursively call function on x and n//2
            
            res = res * res
            return res if x % 2 == 0 else (x * res)
        '''
        
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            
            res = helper(x, n//2)
            res = res * res
            return (res) if n % 2 == 0 else x*res
        
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
        
     