class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        '''
        swap the position of the first and last characters recursively using 2 pointers
        '''
        def swap(l, r, ls):
            if l >= r:
                return
            ls[l], ls[r] = ls[r], ls[l]
            
            return swap(l+1, r-1, ls)
        
        swap(0, len(s)-1, s)