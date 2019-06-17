
# @Title: 环形链表 (Linked List Cycle)
# @Author: 2464512446@qq.com
# @Date: 2019-03-12 12:56:49
# @Runtime: 60 ms
# @Memory: 17.2 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = fast =head
        
        if head is None:
            return False
        if not head.next or not head.next.next:
            return False
        while True:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            elif slow is None or fast is None or fast.next is None:
                return False
