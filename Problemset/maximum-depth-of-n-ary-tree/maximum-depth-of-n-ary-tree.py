
# @Title: N 叉树的最大深度 (Maximum Depth of N-ary Tree)
# @Author: 2464512446@qq.com
# @Date: 2019-10-09 23:05:29
# @Runtime: 844 ms
# @Memory: 105.3 MB

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return self.height(root)
    
    def height(self, node):
        if node is None: return 0
        depth = 0
        for i in node.children:
            depth = max(self.height(i), depth)
        return 1 + depth

    # 迭代实现
    # 执行用时 : 124 ms, 在Maximum Depth of N-ary Tree的Python3提交中击败了48.32% 的用户
    # 内存消耗 : 17.2 MB, 在Maximum Depth of N-ary Tree的Python3提交中击败了99.12% 的用户
    # def maxDepth(self, root: Node) -> int:
    #     if root is None: return 0
    #     queue = [root]
    #     level_size = 1
    #     height = 0
    #     while len(queue):
    #         node = queue.pop(0)
    #         level_size -= 1
    #         if len(node.children):
    #             queue.extend(node.children)
    #         if level_size == 0:
    #             height += 1
    #             level_size = len(queue)
    #     return height
