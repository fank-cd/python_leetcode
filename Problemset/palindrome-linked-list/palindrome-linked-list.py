
# @Title: 回文链表 (Palindrome Linked List)
# @Author: 2464512446@qq.com
# @Date: 2020-10-23 22:03:59
# @Runtime: 76 ms
# @Memory: 23.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow,fast = head,head

        while True:
            if not fast or not fast.next:
                break 
            slow,fast = slow.next,fast.next.next

        fast = slow
        prev,curr = None,fast
        while curr:
            temp = curr.next
            curr.next = prev

            prev,curr = curr,temp

        fast = prev
        slow = head
        # print(fast,slow)
        while fast:
            # print(fast,slow)
            if slow.val != fast.val:
                return False
            slow,fast = slow.next,fast.next
        return True 
