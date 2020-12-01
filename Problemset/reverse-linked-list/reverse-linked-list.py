
# @Title: 反转链表 (Reverse Linked List)
# @Author: 2464512446@qq.com
# @Date: 2020-11-08 00:00:23
# @Runtime: 36 ms
# @Memory: 14.4 MB

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
        if not head:
            return None
        perv,curr = None,head
        while curr:
            temp = curr.next
            curr.next = perv
            perv,curr = curr,temp
        return perv
            
