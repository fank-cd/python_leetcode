
# @Title: 回文链表 (Palindrome Linked List)
# @Author: 2464512446@qq.com
# @Date: 2019-11-19 10:33:55
# @Runtime: 92 ms
# @Memory: 31 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # 思路2： 快慢指针找到中间链表，然后逆序后半部分
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]
