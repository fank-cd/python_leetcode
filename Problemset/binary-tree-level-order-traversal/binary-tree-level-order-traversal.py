
# @Title: 二叉树的层序遍历 (Binary Tree Level Order Traversal)
# @Author: 2464512446@qq.com
# @Date: 2019-12-09 16:00:56
# @Runtime: 24 ms
# @Memory: 12.2 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root, ])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level 
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # go to next level
            level += 1

        return levels



    #     if not root:
    #         return None
        
    #     d = {}
    #     self.level_node(root,d,0)
    #     # print(d)
    #     res = []
    #     for k,v in d.items():
    #         res.append(v)
    #     return res

    # def level_node(self,node,d,level):
    #     if not node:
    #         return None
    #     if level not in d:
    #         d[level] = []
    #     d[level].append(node.val)
    #     self.level_node(node.left,d,level+1)
    #     self.level_node(node.right,d,level+1)

        
