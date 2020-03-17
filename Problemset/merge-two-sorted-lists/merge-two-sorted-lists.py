
# @Title: 合并两个有序链表 (Merge Two Sorted Lists)
# @Author: 2464512446@qq.com
# @Date: 2019-11-04 16:10:45
# @Runtime: 16 ms
# @Memory: 11.8 MB

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
                temp_node = l1
                l1 = l1.next
            else:
                temp_node = l2
                l2 = l2.next

            if not l:
                l = temp_node
                l.next = None
                head = l
            else:
                temp_node.next = None
                l.next = temp_node
                l = l.next
        if l1:
            l.next = l1
        if l2:
            l.next =l2

        return head
