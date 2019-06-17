
# @Title: 删除链表中的节点 (Delete Node in a Linked List)
# @Author: 2464512446@qq.com
# @Date: 2019-03-14 10:57:56
# @Runtime: 52 ms
# @Memory: 11.4 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node.next
        node.val = temp.val
        node.next = temp.next
