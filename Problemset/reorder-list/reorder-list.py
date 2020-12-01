
# @Title: 重排链表 (Reorder List)
# @Author: 2464512446@qq.com
# @Date: 2020-10-20 11:06:01
# @Runtime: 108 ms
# @Memory: 22.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        if not head:
            return 
        p = head
        while p:
            stack.append(p)
            p = p.next
        p1,p2 = 0 ,len(stack)-1
        while p1 < p2:
            stack[p1].next = stack[p2]
            
            p1 += 1
            if p1 == p2:
                break
            stack[p2].next = stack[p1]
            p2 -= 1
        stack[p1].next =  None
            
