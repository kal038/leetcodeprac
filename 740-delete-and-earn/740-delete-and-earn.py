from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''
        bottom up solution, build the array that, at each index, stores the max earning of all values considered up to that point
        for example: [2,3,5,7,8]
        dp array:    [2,3,8,...]in which 8 is the max amount we could earn when considering the subarray [2,3,5]
                        e1,e2
        further optimization, we recognize that we only need to store the value 1 and 2 index in front of the element considered, reduce memory by just using 2pointers and update them e1, e2
        '''
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        e1, e2 = 0, 0
        for i in range(len(nums)):
            curr_e = nums[i] * count[nums[i]] # value * frequency = total earned, from here divide into two cases. 1: the value right before is not a violation -> awesome. 2: the value right before IS a violation -> recurrence relation
            if i > 0 and nums[i] == nums[i-1] + 1: 
                temp = e2
                e2 = max(curr_e + e1, e2)
                e1 = temp #increment e1 to where e2 once was
            else:
                temp = e2
                e2 = curr_e + temp 
                e1 = temp #increment e1 to where e2 once was
                
        return e2