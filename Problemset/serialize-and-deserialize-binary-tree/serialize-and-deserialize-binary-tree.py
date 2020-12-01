
# @Title: 二叉树的序列化与反序列化 (Serialize and Deserialize Binary Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-11-17 11:53:00
# @Runtime: 192 ms
# @Memory: 18 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        if not root:
            return data
        def helper(root):
            data.append(root.val)
            helper(root.left) if root.left else data.append(None)
            helper(root.right) if root.right else data.append(None)
        helper(root)
        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        root = data.pop(0)
        if root is None:
            return None
        root = TreeNode(root)
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
