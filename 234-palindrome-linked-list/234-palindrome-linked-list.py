# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        '''
        brute force solution is to save all elements in a list and spot a palindrome of that list . O(n) time O(n) space
        optimal solution would be a combination of Get Middle of Linked List and Reverse Linked List Problems O(n) time, O(1) space
        
        '''
        # brute force
        arr = []
        curr_node  = head
        while curr_node:
            arr.append(curr_node.val)
            curr_node = curr_node.next
        return arr == arr[::-1]
        
        
    