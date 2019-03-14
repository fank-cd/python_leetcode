# coding:utf-8
# 回文链表
# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
#
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true
#
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路：可以用快慢指针方法取得中间节点，然后反转剩下的节点，和左节点比较
# 我这里是直接用列表存。。思路清晰，方便用脑壳


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = []
        while head:
            l.append(head.val)
            head = head.next
        leng = len(l)
        if leng == 1:
            return True
        if leng % 2 == 0:
            temp = l[leng / 2:]
            temp.reverse()
            if l[:leng / 2] == temp:
                return True
            else:
                return False
        else:
            temp = l[leng / 2 + 1:]
            temp.reverse()
            if l[:leng / 2] == temp:
                return True
            else:
                return False
