import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        '''
        top k frequent is most likely to use a heap here with O(Nlogk) time and O(N+k) space for the hm and the heap
        '''
        count = collections.Counter(nums)
        
        return heapq.nlargest(k, count.keys(), key = count.get)