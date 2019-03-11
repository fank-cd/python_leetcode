# coding:utf-8

# 相同的树

# 给定两个二叉树，编写一个函数来检验它们是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
# 示例 1:
#
# 输入:       1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# 输出: true
#
# 示例 2:
#
# 输入:      1          1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# 输出: false
#
# 示例 3:
#
# 输入:       1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# 输出: false
#


# 递归大法


class Solution(object):

    def same(self, p, q):
        if not q and not p:
            return True
        elif not q or not p:
            return False
        elif p.val == q.val:
            return self.same(p.left, q.left) and self.same(p.right, q.right)

        return False

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.same(p, q)


