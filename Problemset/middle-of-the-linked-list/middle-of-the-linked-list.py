
# @Title: 链表的中间结点 (Middle of the Linked List)
# @Author: 2464512446@qq.com
# @Date: 2020-03-24 14:48:18
# @Runtime: 44 ms
# @Memory: 13.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        p1 = p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        return p1
