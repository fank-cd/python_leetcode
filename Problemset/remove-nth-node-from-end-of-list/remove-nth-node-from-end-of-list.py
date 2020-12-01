
# @Title: 删除链表的倒数第N个节点 (Remove Nth Node From End of List)
# @Author: 2464512446@qq.com
# @Date: 2020-10-24 18:20:52
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            # print(first.val)
            first = first.next

        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next


