#
# 19. Remove Nth Node From End of List
#
# Given a linked list, remove the n-th node from the end of list and return its
# head.
#
# Example:
#     Given linked list: 1 -> 2 -> 3 -> 4 -> 5, and n = 2
#
#     After removing the second node from the end, the linked list becomes
#     1 -> 2 -> 3 -> 5
#
# Note:
#     Given n will always be valid.
#
# Follow up:
#     Could you do this in one pass?
#


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 双指针
    def removeNthNodeFromEnd(self, head, n):
        """
        type head: ListNode
        type n: int
        rtype: ListNode
        """
        tmp = ListNode(0)
        tmp.next = head
        fast = slow = tmp
        while n + 1:
            fast = fast.next
            n -= 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return tmp.next
