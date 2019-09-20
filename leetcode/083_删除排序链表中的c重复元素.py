# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 双指针
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        a, node = ListNode(None), head
        a.next = head
        pre = a
        while node:
            if pre and node.val == pre.val:
                pre.next = node.next
                node = pre.next
                continue
            pre = node
            node = node.next
        return a.next
