
# @Title: 删除链表的节点 (删除链表的节点 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-05-11 17:54:15
# @Runtime: 32 ms
# @Memory: 14 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        curr = head
        pre = None
        if curr.val == val:
            return curr.next

        while curr:
            if curr.val == val:
                pre.next = curr.next
            pre = curr
            curr = curr.next

        return head


# 另一解法：需要给出val是节点才可行，
# 简单来说就是将val的下一个节点的值和next都等于val自己，这样下一个节点其实就没有用了。
# 也能达到删除的目的
# class Solution:
#     def deleteNode(self, head, val):
#         if head is None or val is None:
#             return None
#         if val.next is not None:  # 待删除节点不是尾节点
#             tmp = val.next
#             val.val = tmp.val
#             val.next = tmp.next
#         elif head == val:  # 待删除节点只有一个节点，此节点为头节点
#             head = None
#         else:
#             cur = head    # 待删除节点为尾节点
#             while cur.next != val:
#                 cur = cur.next
#             cur.next = None
#         return head


