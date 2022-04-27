# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        '''
        for linked list I really think that you have to loop through and check every element first before you can delete 
        them in another pass through
        time complex = O(n)
        space complex = O(n)
        '''
        count = {}
        dummy = ListNode(0, next = head)
        while head:
            if head.val not in count:
                count[head.val] = 1
            else:
                count[head.val] += 1
                
            head = head.next
            
        curr = dummy
        while curr and curr.next:
            if count[curr.next.val] > 1:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
        
                