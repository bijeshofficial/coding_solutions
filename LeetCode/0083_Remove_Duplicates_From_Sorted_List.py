# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head == None:
            return head
        
        cur_node = head.next
        prev = head
        
        while cur_node:
            if cur_node.val == prev.val:
                prev.next = cur_node.next
                cur_node = cur_node.next
            else:
                cur_node = cur_node.next
                prev = prev.next
        return head