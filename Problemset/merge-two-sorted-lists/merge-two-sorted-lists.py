
# @Title: 合并两个有序链表 (Merge Two Sorted Lists)
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 15:55:13
# @Runtime: 48 ms
# @Memory: 13.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prevnode = ListNode(-1)
        prev = prevnode
        while l1 and l2:
            if l1.val > l2.val:
                prev.next = l2
                l2 = l2.next
            else:
                prev.next = l1
                l1 = l1.next
            prev = prev.next
        
        prev.next = l1 if l1 else l2
        return prevnode.next
