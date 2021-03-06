class Solution(object):
    def maxArea(self, h):
        
        l, r = 0 , len(h) -1 
        ans = 0
        while l <= r:
            curr_area =  min(h[l], h[r]) * (r-l) 
            ans = max(ans, curr_area)
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return ans
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
        
       
       