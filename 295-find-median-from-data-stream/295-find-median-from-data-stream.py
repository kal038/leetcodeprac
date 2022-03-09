import heapq
class MedianFinder(object):
    '''
    uses a max heap and a min heap while try to keep the two heaps of relatively the same size by rebalancing after adding
    general rule is that the max-heap is the small heap and the min-heap is the large heap
    at each add, add to small heap then check the max element O(1) time to see if that max element is greater than the min element in the large heap
    if yes, move that element to the large heap to balance things out
    time complexity: getting max, min O(1)
    adding/deleting node from heap O(logn)
    '''

    def __init__(self):
        '''
        do note that python only has a min heap implementation in heapq so you have to add negative values to emulate a max heap.
        do remember to return the negative value every time you get value from max heap.
        '''
        self.small = []
        self.large = []

    def addNum(self, num):
        '''
        blindly add to small heap every single time
        '''
        heapq.heappush(self.small, -1 * num)
        
        # check for balancing
        
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            #needs balancing
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        #check for uneven size of greater than 2
        
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) +1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)
        
        

    def findMedian(self):
        '''
        if one heap is larger than the other (should be by one element), return that element
        if they are the same size, return the two top elements divided by 2
        '''
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return float((-self.small[0] + self.large[0])) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()