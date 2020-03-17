
# @Title: 排序链表 (Sort List)
# @Author: 2464512446@qq.com
# @Date: 2019-12-04 16:01:38
# @Runtime: 204 ms
# @Memory: 26.2 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast,slow = fast.next.next, slow.next
        mid = slow.next
        slow.next = None # 把链表切割开
        left,right = self.sortList(head),self.sortList(mid)

        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next ,left = left,left.next
            else:
                h.next ,right = right, right.next
            h = h.next

        h.next = left if left else right
        return res.next
