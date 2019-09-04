# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        li = []
        for i in l1.val:
            li.append(i)
        for i in l2.val:
            li.append(i)
        return li


l1 = ListNode([1,2,3])
l2 = ListNode([1,2,4])
print(l1.val)
a = Solution()
print(a.mergeTwoLists(l1,l2))
