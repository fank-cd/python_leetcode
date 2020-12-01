
# @Title: 填充每个节点的下一个右侧节点指针 (Populating Next Right Pointers in Each Node)
# @Author: 2464512446@qq.com
# @Date: 2020-10-15 10:24:28
# @Runtime: 72 ms
# @Memory: 15 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        stack = [root]
        while stack:
            pre = None
            for i in range(len(stack)):

                node = stack.pop(0)
                if pre:
                    pre.next = node
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                
                pre = node
        return root
