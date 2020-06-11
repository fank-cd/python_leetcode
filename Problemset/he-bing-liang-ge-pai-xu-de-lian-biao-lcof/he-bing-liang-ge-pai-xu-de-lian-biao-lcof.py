
# @Title: 合并两个排序的链表 (合并两个排序的链表  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-10 18:11:39
# @Runtime: 60 ms
# @Memory: 14.1 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
            
        l = None
        head = l
        while l1 and l2:
            if l1.val < l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2 
                l2 = l2.next

            if not l: # 初始化链表
                l = temp
                l.next = None
                head = l
            else:
                temp.next = None
                l.next = temp
                l= l.next

        if l1:
            l.next = l1
        if l2:
            l.next = l2 

        return head
