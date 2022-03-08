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
        '''
        bucket sort solution O(n) time and O(n) space
        
        create a list that the frequency corresponds to the indicies: [[],[],[],[], ..., []]
                                                                        0  1  2  3        n
        then traverse this list from right to left while adding values to a result list until len(result) == k
        
        
        '''
        count = collections.Counter(nums)
        freq = [[] for x in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        print(freq)
        res = []
        for i in range(len(freq))[::-1]:
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res