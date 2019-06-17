
# @Title: 二叉树的层次遍历 (Binary Tree Level Order Traversal)
# @Author: 2464512446@qq.com
# @Date: 2018-12-18 10:14:47
# @Runtime: 32 ms
# @Memory: 7.7 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        res =[]
        d = []
        node = root
        d.append(node)
        while d:
            templist = []
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
