class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        create a decision tree so that at reach level the number of subsets increase by 2 times
        this decision tree could choose to include or not include an element starting with the first element
        height of the tree is: n (n = len(nums))
        each level is: 2^n
        time complexity: O(n*(2^n))
        '''
        curr = []
        res = []
        def backtrack(i):
            if i >= len(nums):
                res.append(curr[:])
                return
            
            #include i-th element
            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()
            backtrack(i + 1)
            
        backtrack(0)
        return res
        