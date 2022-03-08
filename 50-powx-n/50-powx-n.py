class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        t=abs(n)
        ans=1
        while(t>0):
            if(t%2==0):
                x=x*x
                t=t//2
            else:
                ans=ans*x
                t=t-1
        if(n<0):
            return 1/ans
        else:
            return ans