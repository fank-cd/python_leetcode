
# @Title: 从尾到头打印链表 (从尾到头打印链表 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-07-22 14:27:51
# @Runtime: 60 ms
# @Memory: 24.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        p = head
        def helper(p):
            if not p:
                return None
            helper(p.next)
            res.append(p.val)
        
        helper(p)
        return res
