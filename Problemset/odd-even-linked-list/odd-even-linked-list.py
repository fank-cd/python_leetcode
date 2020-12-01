
# @Title: 奇偶链表 (Odd Even Linked List)
# @Author: 2464512446@qq.com
# @Date: 2020-11-13 10:25:29
# @Runtime: 52 ms
# @Memory: 15.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        evenhead = head.next
        odd,even = head,evenhead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenhead

        return head
