class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''
        topdown dynamic programming solution using @lru_cache to memoize the recursive call
        '''
        
        points = defaultdict(int)
     
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
        
        @lru_cache
        def max_points(num):
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            
            return max(max_points(num - 1), max_points(num-2) + points[num]) #either don't take the current value and take the previous' or take the current and the one 2 units away
        
        return max_points(max(nums))