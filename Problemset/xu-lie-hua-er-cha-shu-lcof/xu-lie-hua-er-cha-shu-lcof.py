
# @Title: 序列化二叉树 (序列化二叉树  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-07-03 18:12:06
# @Runtime: 228 ms
# @Memory: 17.8 MB

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
        if not root:
            return None
        data = []
        # sys.stdout.write(str(root.val))
        def helper(root):
            data.append(root.val)
            if root.left:
                helper(root.left)
            else:
                data.append(None)

            if root.right:
                helper(root.right)
            else:
                # sys.stdout.write('$')
                data.append(None)
        helper(root)
        return data


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not isinstance(data, list) or len(data) == 0:
            return

        if data[0] == None:
            node = None
        else:
            node = TreeNode(int(data[0]))
        data.pop(0)
        if node:
            node.left = self.deserialize(data)
            node.right = self.deserialize(data)
        # print(type(node))
        return node
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
