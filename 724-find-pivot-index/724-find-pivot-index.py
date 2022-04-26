class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        brute force through this mf
        for loop through and calculate the left and right sums and compare if they equal
        '''
#         if len(nums) == 1: return 0
#         for i in range(len(nums)):
#             #print(nums[:i])
#             left_sum = sum(nums[:i]) if i != 0 else 0
#             right_sum = sum(nums[i+1:]) if i != (len(nums) - 1) else 0
#             if left_sum == right_sum:
#                 return i 
#         return -1

        '''
        time limit exceeded
        have to use other methods
        '''
        total = sum(nums)
        
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] -leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
        
        
        