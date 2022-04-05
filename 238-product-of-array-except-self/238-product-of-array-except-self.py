
class Solution(object):
    def prod(self,arr):
        if len(arr) == 1:
            return arr[0]
        res = 1
        for i in range(len(arr)):
            res *= arr[i]
        return res
    def productExceptSelf(self, nums):
        """
        The tricky part about the problem is that you can't use division to divide off the curr element
   
        My 1st approach will work but runs to slow, so need a second approach
        
        Ingeniousity: create a L and R arrays that store either all products to the left of idx i and to the right of idx i
        multiply them together to create ans
        
         [4,5,1,8,2]
        L = [1,4,20,20,160]
        R = [80,16,16,2,1 ]
        """
        
#         L,R, res = [1 for _ in range(len(nums))],  [1 for _ in range(len(nums))],  [1 for _ in range(len(nums))]
#         for i in range(1, len(nums)):
#             L[i] = self.prod(nums[:i])
#         for j in range(len(nums)-1):
#             R[j] = self.prod(nums[j+1:])
#         for k in range( len(res)):
#             res[k]= L[k] * R[k]
            
#         return res

        res = [1]
        val = 1
        for i in range(len(nums)-1):
            val *= nums[i]
            res.append(val)
        val = 1
        for j in range(len(nums)-1, 0, -1):
            val *= nums[j]
            res[j-1] *= val
        return res
                