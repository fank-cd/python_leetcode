
# @Title: 二叉树的锯齿形层次遍历 (Binary Tree Zigzag Level Order Traversal)
# @Author: 2464512446@qq.com
# @Date: 2019-12-18 16:44:53
# @Runtime: 20 ms
# @Memory: 12.2 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
                
        if not root:
            return None
        res = []
        stack1 = [root]
        stack2 = []
        while stack1 or stack2:
            cur_list  = []
            if stack1:
                while stack1:
                    cur = stack1.pop()
                    cur_list.append(cur.val)
                    if cur.left:
                        stack2.append(cur.left)
                    if cur.right:
                        stack2.append(cur.right)
                


            else:
                while stack2:
                    cur = stack2.pop()
                    cur_list.append(cur.val)
                    if cur.right:
                        stack1.append(cur.right)
                
                    if cur.left:
                        stack1.append(cur.left)
            res.append(cur_list)

        return res


