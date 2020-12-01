
# @Title: N 叉树的层序遍历 (N-ary Tree Level Order Traversal)
# @Author: 2464512446@qq.com
# @Date: 2020-11-16 15:12:29
# @Runtime: 64 ms
# @Memory: 15.3 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            level = []
            for i in range(len(stack)):
                cur = stack.pop(0)
                level.append(cur.val)
                stack.extend(cur.children)
            res.append(level)
        return res
