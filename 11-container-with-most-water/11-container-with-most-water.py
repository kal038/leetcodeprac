class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        
        '''
        initialize a pointer at front and a pointer at end
        check the insides, if have taller than move pointer
        return the result min(height[l], height[r]) * (r-l) 
        
        this approach is wrong because there could be a high pillar in the middle and our pointers
        would not be able to get there
        '''
        '''
        """
        if len(h) == 1: return 0
        l , r = 0, len(h) - 1
        ans = 0
        while (l < r):
            ans = max(ans, min(h[l], h[r]) * (r-l))
            if h[l]  < h[r]:
                # want to keep the taller pillar
                l += 1
            else:
                r -= 1
            
        return ans  # r-l is going to produce 0 if they are on the same index