# coding:utf-8
# 合并有序链表


# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路是先判断l1和l2都存在，或者l1\l2d都不存在,或者只存在其中一个的情况，依此来确定头结点

# 确定头结点后，确定头结点的往后移动一位
# 此时可能存在l1或者l2已经为空的情况，如果为空，则直接将剩下的l1或者l2连接上
# 如果l1 和l2 都还存在，则判断大小，拼接至头结点，然后往后移动一位，以表示这个点已经用过了这样


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            if l1.val > l2.val:
                head = l2
                l2 = l2.next
            elif l1.val <= l2.val:
                head = l1
                l1 = l1.next
        elif not l1 and not l2:
            return []
        elif not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1

        head_temp = head
        while l1 or l2:
            if l1 and l2:
                # print l1
                if l1.val < l2.val:
                    head_temp.next = l1
                    l1 = l1.next
                    head_temp = head_temp.next
                    # print "l1"
                    # print head_temp.val
                elif l1.val >= l2.val:
                    head_temp.next = l2
                    l2 = l2.next
                    head_temp = head_temp.next
                    # print "l2"
                    # print head_temp.val
            elif l1 and not l2:
                head_temp.next = l1
                # print head_temp.next.val
                break

            elif not l1 and l2:
                head_temp.next = l2
                break
        # print head_temp.val

        return head


