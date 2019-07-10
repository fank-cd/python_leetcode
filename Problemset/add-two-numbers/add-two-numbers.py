
# @Title: 两数相加 (Add Two Numbers)
# @Author: 2464512446@qq.com
# @Date: 2019-07-09 15:37:48
# @Runtime: 104 ms
# @Memory: 13.7 MB

#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        直接链表相加来解决的，方法比较蠢，需要考虑几种情况
        1、l1 或者l2 为空的情况
        2、相加进位后再相加再次进位的情况
        3、只有一边有值得情况
        代码写的比较粗糙，我认为是体力活
        """
        q = l1
        p = l2
        r = ListNode(None)
        head = r
        carry = 0
        while (q or p) or carry ==1:
            if q and p:
                print(carry)
                q_tmp = q.val
                p_tmp = p.val
                tmp = (q_tmp+p_tmp+carry) %10
                r.val = tmp
                carry = 0


                carry += 1 if tmp < (q_tmp+p_tmp) else 0

                if q.next or p.next:
                    r.next = ListNode(None)
                    r = r.next
                q = q.next
                p = p.next

            elif q and not p:
                tmp = (q.val+carry) %10
                r.val = tmp
                carry = 0
                carry += 1 if tmp < (q.val+carry) else 0
                q = q.next
                if q or p:
                    r.next = ListNode(None)
                    r = r.next
               

            elif not q and p:
                tmp = (p.val+carry) %10
                r.val = tmp
                carry = 0
                carry += 1 if tmp < (p.val+carry) else 0

                p = p.next
                if q or p:
                    r.next = ListNode(None)
                    r = r.next


            elif not q and not p:
                print(carry)
                r.next = ListNode(None)
                r = r.next
                r.val = carry
                carry = 0
            
        return head
        

