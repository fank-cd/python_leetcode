
# @Title: 二叉搜索树的范围和 (Range Sum of BST)
# @Author: 2464512446@qq.com
# @Date: 2019-09-06 15:00:00
# @Runtime: 604 ms
# @Memory: 27.4 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not isinstance(root,TreeNode) or not isinstance(L,int) or not isinstance(R,int):
            return 0

        
        if root.val>= L and root.val <= R:
            return root.val + self.rangeSumBST(root.right,L,R) + self.rangeSumBST(root.left,L,R)
        elif root.val < L:
            return self.rangeSumBST(root.right,L,R)
        elif root.val > R:
            return self.rangeSumBST(root.left,L,R)
            
        return count


