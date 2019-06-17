
# @Title: 回文链表 (Palindrome Linked List)
# @Author: 2464512446@qq.com
# @Date: 2019-03-14 10:44:02
# @Runtime: 144 ms
# @Memory: 30.1 MB

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
        l = []
        while head:
            l.append(head.val)
            head = head.next
        leng = len(l)
        if leng ==1:
            return True
        if leng %2 == 0:
            temp = l[leng/2:]
            temp.reverse()
            if l[:leng/2] == temp:
                return True
            else:
                return False
        else:
            temp = l[leng/2+1:]
            temp.reverse()
            if l[:leng/2] == temp:
                return True
            else:
                return False
            
