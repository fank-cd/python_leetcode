
# @Title: 删除链表的倒数第N个节点 (Remove Nth Node From End of List)
# @Author: 2464512446@qq.com
# @Date: 2019-03-05 10:13:31
# @Runtime: 28 ms
# @Memory: 10.8 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
            leng +=1
            temp1= temp1.next
        
        if leng == n :
            head = head.next
            return head
        temp2 = head
        for i in range(leng-n-1):
            temp2 = temp2.next
        temp = temp2.next
        if temp:
            temp2.next = temp.next
        elif not temp:
            head = None
        return head
        
