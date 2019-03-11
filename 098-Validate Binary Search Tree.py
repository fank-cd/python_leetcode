# coding:utf-8
# 验证二叉搜索树
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
#     节点的左子树只包含小于当前节点的数。
#     节点的右子树只包含大于当前节点的数。
#     所有左子树和右子树自身必须也是二叉搜索树。
#
# 示例 1:
#
# 输入:
#     2
#    / \
#   1   3
# 输出: true
#
# 示例 2:
#
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。根节点的值为 5 ，但是其但是其右子节点值为 4 。


# 思路：二叉树来遍历一定是没有问题的，问题在于要求左子树必小于当前节点,递归解决
# 右子树只包含大于当前节点

# 那么调用时则将左子树的small（也就是最小值）调用为small，最大值调用为当前节点，则必不能大于当前节点否则返回false
# 右子树同理

class Solution(object):

    def validBST(self, root, small, large):
        if root == None:
            return True
        if small >= root.val or large <= root.val:  # 判定边界
            return False
        return self.validBST(root.left, small, root.val) and self.validBST(root.right, root.val, large)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validBST(root, -2 ** 32, 2 ** 32 - 1)
