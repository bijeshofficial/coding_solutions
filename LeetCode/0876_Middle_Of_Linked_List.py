# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        l = []
        cur_node = head
        while cur_node:
            l.append(cur_node)
            cur_node = cur_node.next
            
        return (l[len(l)//2])

#Fast and Slow Pointer Approach which 
class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow