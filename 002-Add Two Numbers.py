# coding:utf-8

# 两数相加


# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


# 我这个代码太丑了。。
# 思路是先翻转链表，得到相加的数字
# 再构建一个新链表
# 。。辣鸡代码

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):

        if head:
            p = head
            q = head.next
            p.next = None

            while q:
                r = q.next
                q.next = p
                p = q
                q = r
            return p
        else:
            return None

    def listtoint(self, l):
        leng = len(l)

        wei = 10 ** (leng - 1)
        res = 0
        for i in range(leng):
            res += l[i] * wei
            wei = wei / 10
        return res

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        num1 = []
        num2 = []

        while l1:
            num1.append(l1.val)
            l1 = l1.next

        while l2:
            num2.append(l2.val)
            l2 = l2.next

        res = self.listtoint(num1) + self.listtoint(num2)
        res = str(res)[::-1]
        leng = len(res)
        head = ListNode(int(res[0]))
        # print head

        temp = head
        if head:
            for i in range(1, leng):
                temp.next = ListNode(int(res[i]))
                temp = temp.next

        return head
