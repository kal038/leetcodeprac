class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Quick select algorithm with an average run time of O(n)
        This happens when the pivot that you pick actually lies in the middle of the values
        If the value that you pick every single time happens to be the largest/lowest
        value of that iteration then it is the worst time complexity of O(n^2)
        Algorithm:
            Choose rightmost element as pivot
            Initialize p pointer as leftmost pointer of the sub-array we are considering
            Compare the value at p pointer to pivot and determine position accordingly
            Run quick select again recursively until the position of (p pointer == len(nums) - k), that is the k-th largest element of the array 
        '''
        k = len(nums) - k # reassign k to be the exact idx that p has to be in order to terminate
        
        def quickselect(l, r):
            '''
            l and r pointers allow for us to choose what subarrray to look at
            '''
            pivot, p = nums[r], l #initialize pivot to rightmost value and p to leftmost idx
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
         
            if p > k: return quickselect(l, p - 1)
            elif p < k: return quickselect(p + 1, r)
            else:
                return nums[k]
                
        return quickselect(0, len(nums) - 1)