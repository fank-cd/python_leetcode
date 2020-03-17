
# @Title: 反转链表 (Reverse Linked List)
# @Author: 2464512446@qq.com
# @Date: 2019-08-28 16:08:04
# @Runtime: 24 ms
# @Memory: 13.5 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next

        return rev
