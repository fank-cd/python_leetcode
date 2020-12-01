
# @Title: 反转链表 (反转链表 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-04-20 17:19:13
# @Runtime: 44 ms
# @Memory: 14.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        #         巧妙利用python的多元赋值
#         多元赋值的时候，右边的值不会随着赋值而改变
#         p, rev = head, None
#         while p:
#             rev, rev.next, p = p, rev, p.next
#         return rev

        # stack = [None]
        # while p:
        #     stack.append(p)
        #     p = p.next
        # head = stack.pop()
        # p = head
        # while p:
        #     p.next = stack.pop()
        #     p = p.next
        # return head

        curr,prev = head, None
        while curr:
            temp = curr.next
            # print(temp)
            curr.next = prev
            # prev = curr
            # curr = temp
            prev,curr = curr,temp
        return prev
