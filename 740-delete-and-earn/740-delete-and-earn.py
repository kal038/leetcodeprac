class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''
        topdown dynamic programming solution using @lru_cache to memoize the recursive call
        '''
        
        points = defaultdict(int)
        max_number = 0
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
            
        print(points)
        print(max_number)
        @cache
        def max_points(num):
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            
            return max(max_points(num - 1), max_points(num-2) + points[num])
        
        return max_points(max_number)