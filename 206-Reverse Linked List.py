# coding:utf-8

# 反转链表

# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#

# 前中后三个指针反转

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            p = head
            q = head.next
            p.next = None

            while q:
                r= q.next
                q.next = p
                p = q
                q = r
            return p
        else:
            return None