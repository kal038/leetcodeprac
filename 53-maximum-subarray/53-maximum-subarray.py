class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = nums[0]
        max_subarray = nums[0]
        for i in range(1, len(nums)):
            if current_subarray < 0:
                current_subarray = nums[i]
                if nums[i] > max_subarray:
                    max_subarray = nums[i]
                continue
            
            current_subarray += nums[i]
           
            
            max_subarray = max(max_subarray, current_subarray)
               
        
        
        
        
        return max_subarray
       
            