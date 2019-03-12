# coding:utf-8
# 二叉树的层次遍历
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 返回其层次遍历结果：
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 层次遍历，其实我觉得和101挺像的，都可以用一个栈遍历
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        res = []  # 最终结果的列表
        d = []  # 存待遍历的节点
        node = root
        d.append(node)
        while d:
            templist = []  # 已经遍历过的节点 最后append到res中
            templen = len(d)
            for i in xrange(templen):
                # print d
                node = d.pop(0)
                templist.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res.append(templist)
        return res