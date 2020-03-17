
# @Title: N叉树的前序遍历 (N-ary Tree Preorder Traversal)
# @Author: 2464512446@qq.com
# @Date: 2019-09-28 18:31:42
# @Runtime: 748 ms
# @Memory: 107.4 MB

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 递归
        # res = []
        # if not isinstance(root,Node):
        #     return res
        # res.append(root.val)
        # for child in root.children:
        #     res += self.preorder(child)

        # return res

        if not isinstance(root, Node):
            return []
        res = []
        stack = [root]
        while stack:
            temp = stack.pop()
            res.append(temp.val)
            if temp.children:

                stack.extend(temp.children[::-1])

        return res
