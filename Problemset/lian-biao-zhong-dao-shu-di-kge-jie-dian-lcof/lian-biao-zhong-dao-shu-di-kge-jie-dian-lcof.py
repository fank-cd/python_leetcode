
# @Title: 链表中倒数第k个节点 (链表中倒数第k个节点 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-09 18:12:04
# @Runtime: 40 ms
# @Memory: 13.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p1 = head
        p2 = head
        for i in range(k):
            p2 = p2.next
        if not p2:
            return head
        ## print(p2.val)
        while p2:
            p1 = p1.next
            p2 = p2.next
        return p1
