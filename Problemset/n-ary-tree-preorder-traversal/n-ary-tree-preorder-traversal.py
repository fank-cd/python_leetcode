
# @Title: N叉树的前序遍历 (N-ary Tree Preorder Traversal)
# @Author: 2464512446@qq.com
# @Date: 2020-11-16 15:14:04
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
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            cur = stack.pop()
            stack.extend(cur.children[::-1])
            res.append(cur.val)
        return res
