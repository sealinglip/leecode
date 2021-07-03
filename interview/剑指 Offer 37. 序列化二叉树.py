# 请实现两个函数，分别用来序列化和反序列化二叉树。
# 你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
# 提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

#  
# 示例：
# 输入：root = [1, 2, 3, null, null, 4, 5]
# 输出：[1, 2, 3, null, null, 4, 5]
from treenode import TreeNode
from collections import deque


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
        stack = deque()
        stack.append(root)  # 根节点
        valList = []
        while stack:
            node = stack.popleft()
            valList.append(str(node.val) if node else 'N')
            if node:
                stack.extend([node.left, node.right])

        return ','.join(valList)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodeList = []
        for v in data.split(','):
            nodeList.append(TreeNode(int(v)) if v != 'N' else None)

        depth = [nodeList[0]]  # 逐层构建
        i = 1
        l = len(nodeList)
        while depth and i < l:
            newDepth = []
            for node in depth:
                left = nodeList[i]
                if left:
                    node.left = left
                    newDepth.append(left)
                i += 1

                if i >= l:
                    break

                right = nodeList[i]
                if right:
                    node.right = right
                    newDepth.append(right)
                i += 1

                if i >= l:
                    break

            depth = newDepth

        return nodeList[0]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == "__main__":
    codec = Codec()
    codec.deserialize(codec.serialize(TreeNode.createBFSTree([2, 3, 1])))
