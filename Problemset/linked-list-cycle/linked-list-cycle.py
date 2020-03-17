
# @Title: 环形链表 (Linked List Cycle)
# @Author: 2464512446@qq.com
# @Date: 2019-11-13 12:14:19
# @Runtime: 44 ms
# @Memory: 18.3 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # if not head:
        #     return False
        # while head.next and head.val != None:
        #     head.val = None
        #     head = head.next
        # if not head.next:
        #     return False
        # return True

        if not isinstance(head,ListNode):
            return False
        p1, p2= head, head.next
        while p1 and p2 and p2.next:
            if p1 == p2:
                return True
            p1 = p1.next
            p2 = p2.next.next
        return False
