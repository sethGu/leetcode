# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pre,aft=head,head
        while aft and aft.next:
            pre=pre.next
            aft=aft.next.next
            if pre==aft: return True
        return False