class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0 
        while n>0:
        # it just checks if right bit is set or not 
            if n&1: 
                ans +=1 

            # removes the last bit 
            n>>=1    

        return ans
