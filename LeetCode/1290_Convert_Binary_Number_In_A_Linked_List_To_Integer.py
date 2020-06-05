# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur_node = head
        elems = ''
        while cur_node != None:
            elems += str(cur_node.val)
            cur_node = cur_node.next
        return int(elems,2)