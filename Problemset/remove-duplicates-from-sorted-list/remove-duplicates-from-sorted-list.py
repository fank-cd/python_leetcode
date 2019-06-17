
# @Title: 删除排序链表中的重复元素 (Remove Duplicates from Sorted List)
# @Author: 2464512446@qq.com
# @Date: 2019-03-11 11:03:05
# @Runtime: 40 ms
# @Memory: 10.8 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        if temp:
            while temp.next:
                if temp.val == temp.next.val:
                    temp.next = temp.next.next
                else:
                    temp =temp.next
                if not temp:
                    break

        return head
            
            
