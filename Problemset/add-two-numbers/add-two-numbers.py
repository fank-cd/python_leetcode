
# @Title: 两数相加 (Add Two Numbers)
# @Author: 2464512446@qq.com
# @Date: 2019-03-19 10:11:56
# @Runtime: 104 ms
# @Memory: 10.9 MB

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
                r= q.next
                q.next = p
                p = q
                q = r
            return p
        else:
            return None

    def listtoint(self, l):
        leng = len(l)
        
        wei = 10**(leng-1)
        res = 0
        for i in range(leng):
            res += l[i] *wei
            wei= wei/10
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
        leng =len(res)
        head = ListNode(int(res[0]))
        # print head
        
        temp = head
        if head:
            for i in range(1,leng):
                temp.next = ListNode(int(res[i]))
                temp = temp.next
                
        return head
        
