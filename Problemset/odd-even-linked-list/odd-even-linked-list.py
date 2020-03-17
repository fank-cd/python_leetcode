
# @Title: 奇偶链表 (Odd Even Linked List)
# @Author: 2464512446@qq.com
# @Date: 2019-12-09 12:06:43
# @Runtime: 32 ms
# @Memory: 15.2 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        count = 1
        odd_node, even_node = None, None  # 奇数节点，偶数节点
        even_head = None # 偶数头节点
        # 节点不存在和只有一个节点的情况
        if not head or head.next is None:
            return head
        while p:
            if count % 2 !=0:  # 奇数节点
                if odd_node:
                    odd_node.next = p
                odd_node = p
                if not p.next: # 结尾在奇数节点，合并后是偶数节点的next为None
                    even_node.next = None
            else:
                if even_node:  # 偶数节点
                    even_node.next = p
                if count == 2:  # 偶数头结点
                    even_head = p
                even_node = p
                if not p.next: # 结尾在偶数节点，合并后是奇数节点的next为None
                    odd_node.next = None
            count +=1
            p = p.next
        p = head
        while p.next: # 找到奇数链表的末尾节点
            p = p.next
        p.next = even_head # 合并奇数链表和偶数链表
        return head
