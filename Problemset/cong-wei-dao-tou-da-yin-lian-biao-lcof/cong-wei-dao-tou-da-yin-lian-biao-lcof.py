
# @Title: 从尾到头打印链表 (从尾到头打印链表 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-03-17 15:09:05
# @Runtime: 24 ms
# @Memory: 25.5 MB

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
