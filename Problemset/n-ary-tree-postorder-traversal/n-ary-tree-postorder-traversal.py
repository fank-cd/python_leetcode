
# @Title: N叉树的后序遍历 (N-ary Tree Postorder Traversal)
# @Author: 2464512446@qq.com
# @Date: 2020-12-01 16:57:09
# @Runtime: 56 ms
# @Memory: 15.2 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        res = []
        if not root:
            return res
        def helper(root):
            if root.children:
                for i in root.children:
                    helper(i)
            
            res.append(root.val)
        helper(root)
        return res
