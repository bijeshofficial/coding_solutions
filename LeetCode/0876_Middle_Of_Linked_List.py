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