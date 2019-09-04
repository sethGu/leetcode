class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:
        """

        :param head:
        :return:
        """

        if head == None: return
        pre = None  # 0
        while head.next:
            nex = head.next # 1
            head.next = pre # 0
            pre = head  # 0
            head = nex # 1
        head.next = pre # 0
        return head

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

# 或者
    class Solution:
        def reverseList(self, head: ListNode) -> ListNode:
            if head == None: return
            L, M, R = None, None, head
            while R.next != None:
                L = M
                M = R
                R = R.next
                M.next = L
            R.next = M
            return R
