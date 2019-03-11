# coding:utf-8
# 删除排序链表中的重复元素
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
#
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3
#

# 感觉没有啥可说的
# 思路： 1 当前元素跟下个元素对比 2 相等移动当前元素的下个元素指针 3 不相等移动当前元素指针

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        temp = head
        if temp:
            while temp.next:
                if temp.val == temp.next.val:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
                if not temp:
                    break

        return head

