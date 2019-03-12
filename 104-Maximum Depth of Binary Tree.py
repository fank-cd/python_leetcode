# coding:utf-8
# 二叉树的最大深度

# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 返回它的最大深度 3 。

# 递归写法 简洁明了

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        lep = self.maxDepth(root.left)
        rep = self.maxDepth(root.right)

        return max(lep, rep) + 1