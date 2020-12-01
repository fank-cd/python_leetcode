
# @Title: 删除链表中的节点 (Delete Node in a Linked List)
# @Author: 2464512446@qq.com
# @Date: 2019-09-06 11:48:29
# @Runtime: 28 ms
# @Memory: 11.9 MB

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
        node.val,node.next = node.next.val,node.next.next
