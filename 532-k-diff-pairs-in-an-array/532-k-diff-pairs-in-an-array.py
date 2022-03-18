import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        The problem includes finding a pair in an array that have a value of 2 when subtracted with each other
        Idea:
            Have a l and r pointers point at 1st and 2nd element 
            while l<r:
                if l == r:
                    r += 1
                else
                evaluate abs(l-r):
                    if < k: r += 1
                    elif > k : l += 1
                    else: res += 1
                    
            return res
                    
        """
        
        
        '''
        [1,3,4,5]
         l r
        
        '''
        
        if k == 0:
            res = 0
            count = collections.Counter(nums)
            print(count)
            for val in count:
                if count[val] > 1:
                    res += 1
            return res
        new = list(set(nums))
        new = sorted(new)
        res = 0
        l = 0
        r = 1
        while l < len(new) and r < len(new):
            if l == r:
                r += 1
            else:
                val = abs(new[l] - new[r])
                if val < k:
                    r += 1
                elif val > k:
                    l += 1
                else:
                    l += 1
                    res += 1
                    
        return res
        