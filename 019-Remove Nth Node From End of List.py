# coding:utf-8
# 删除链表的倒数第N个节点

# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#
# 说明：
#
# 给定的 n 保证是有效的。
#

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 基本思路是先计算出链表的长度，然后排除掉需要删除头节点的情况
# 再遍历下去 找到倒数n-1个节点，确定倒数n节点是否存在，然后temp2.next = temp.next
# (temp2 倒数第n-1个节点，temp 倒数n节点)
#

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp1 = head
        leng = 0
        if temp1.next:
            leng = 1
        while temp1.next:
            leng += 1
            temp1 = temp1.next  # 计算链表长度

        if leng == n:  # 如果要删除的是第一个节点
            head = head.next
            return head

        temp2 = head
        for i in range(leng - n - 1):
            temp2 = temp2.next  # 倒数n-1个节点
        temp = temp2.next  # 倒数n个节点
        if temp:
            temp2.next = temp.next
        elif not temp:
            head = None
        return head
