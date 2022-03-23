# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersect(self, head):
        if head == None:
            return False
        #tortoise and hare
        tortoise = head
        hare = head
        
        while hare is not None and hare.next is not None:            
                        
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return hare
            
        return None
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        Run the tortoise and hare algorithm, that's where the intersect is, from the intersection, have two pointers, 1 from intersect and 1
        from head, traverse until they meet -> cycle start
        '''
        
        if not head:
            return None
        
        inter = self.getIntersect(head)
        if not inter:
            return None
        ptr1 = head
        ptr2 = inter
        
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return ptr1
        
        