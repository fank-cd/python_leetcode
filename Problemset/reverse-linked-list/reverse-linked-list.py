
# @Title: 反转链表 (Reverse Linked List)
# @Author: 2464512446@qq.com
# @Date: 2018-11-19 14:40:21
# @Runtime: 32 ms
# @Memory: N/A

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
        if head:
            p = head
            q = head.next
            p.next = None

            while q:
                r= q.next
                q.next = p
                p = q
                q = r
            return p
        else:
            return None
