
# @Title: 环形链表 (Linked List Cycle)
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 15:24:04
# @Runtime: 60 ms
# @Memory: 16.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        while True:
            if not fast or not fast.next:
                return False
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False
d.next:
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
