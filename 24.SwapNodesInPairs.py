#
# 24. Swap Nodes in Pairs
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
#
# Example:
#     Given 1 -> 2 -> 3 -> 4, you should return the list as 2 -> 1 -> 4 -> 3.
#


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 迭代
    def swapPairs(self, head):
        """
        type head: ListNode
        rtype: ListNode
        """
        prefix = ListNode(0)
        prefix.next = head
        cur = prefix
        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            cur.next = second
            first.next = second.next
            second.next = first
            cur = first
        return prefix.next

    # 递归
    def swapPairs(self, head):
        """
        type head: ListNode
        rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        right = head.next
        head.next = self.swapPairs(right.next)
        right.next = head
        return right
