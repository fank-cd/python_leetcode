
# @Title: 对链表进行插入排序 (Insertion Sort List)
# @Author: 2464512446@qq.com
# @Date: 2020-11-20 11:30:26
# @Runtime: 168 ms
# @Memory: 15.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        last = head
        cur = last.next
        while cur:
            if last.val <= cur.val:
                last = last.next
            else:
                prev  = dummy
                while prev.next.val <= cur.val:
                    prev = prev.next
                
                last.next = cur.next
                cur.next = prev.next
                prev.next = cur
            cur = last.next
        return dummy.next
