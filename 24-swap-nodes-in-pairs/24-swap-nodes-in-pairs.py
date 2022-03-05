# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        Don't need to define an inner function because we don't have to pass extra info into it.
        Recurisve solution
        Time complexity: O(N)
        Space Complexity: O(N) reserved on the call stack
        '''
        
        if not head or not head.next:
            return head
        temp = head.next.next
        ret = head.next
        head.next.next = head;
        head.next = self.swapPairs(temp)
        return ret