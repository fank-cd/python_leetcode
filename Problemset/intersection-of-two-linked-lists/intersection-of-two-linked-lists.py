
# @Title: 相交链表 (Intersection of Two Linked Lists)
# @Author: 2464512446@qq.com
# @Date: 2019-11-06 15:28:23
# @Runtime: 212 ms
# @Memory: 41.6 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pA, pB = headA,headB
        
        while pA != pB:
            # print(pA,pB)
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA 

