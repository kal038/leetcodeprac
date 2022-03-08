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
        
        Pseudocode:
            create a counter dictionary to count the frequency of the values in nums
            insert those values in a heap and extract the k largest values with the return values as they keys of the Counter and the sorting criteria as the value of the Counter using count.get (which return a comparable object (the frequency))
            
        Syntax:
        heapq.nlargest(k, [things to return], [sotring criteria in terms of a function called with no ()])
        '''
        count = collections.Counter(nums)
        
        print(count.get(1))
        print(count.get(2))
        print(count.get(3))
        
        return heapq.nlargest(k, count.keys(), key = count.get) #key = [3,2,1]