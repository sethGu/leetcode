# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None: return True
        L, M, R = None, None, head
        if head.next is None: return True
        else:
            #if head.next == head: return True
            while head.next != None:
                L = M
                M = R
                R = head.next
                M.next = R
                if M == R:
                    if R.next == L: return True
                    elif R.next is None: return True
                    else: return False
            # L.next = M
            # M.next = R

# 快慢指针
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow,fast,prev = head,head,None
        while fast is not None:
            slow = slow.next
            fast = fast.next.next if fast.next is not None else fast.next
        while slow is not None:
            slow.next, slow, prev= prev, slow.next, slow
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

