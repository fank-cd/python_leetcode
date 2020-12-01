
# @Title: 环形链表 II (Linked List Cycle II)
# @Author: 2464512446@qq.com
# @Date: 2020-10-26 17:23:04
# @Runtime: 60 ms
# @Memory: 16.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow,fast = head,head
        while True:
            if not fast or not fast.next:
                return 
            slow,fast =slow.next,fast.next.next
            if slow == fast:
                break
        
        slow = head
        while fast != slow:
            fast,slow =  fast.next, slow.next
        return fast
