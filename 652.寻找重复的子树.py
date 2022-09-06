#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#
# 给定一棵二叉树 root，返回所有重复的子树。

# 对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

# 如果两棵树具有相同的结构和相同的结点值，则它们是重复的。


# 示例 1：
# 输入：root = [1, 2, 3, 4, None, 2, 4, None, None, 4]
# 输出：[[2, 4], [4]]

# 示例 2：
# 输入：root = [2, 1, 1]
# 输出：[[1]]

# 示例 3：
# 输入：root = [2, 2, 2, 3, None, 3, None]
# 输出：[[2, 3], [3]]


# 提示：
# 树中的结点数在[1, 10 ^ 4]范围内。
# -200 <= Node.val <= 200

from typing import Optional, List
from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        cache = {}
        duplicates = set()

        # 设计一种特征表达，能够唯一确定一颗树（子树）
        def serialize(node: TreeNode) -> str:
            if node is None:
                return ''
            encoded = "".join([str(node.val), '(', serialize(
                node.left), ')(', serialize(node.right), ')'])
            if (dup := cache.get(encoded, None)):
                duplicates.add(dup)
            else:
                cache[encoded] = node

            return encoded

        serialize(root)
        return list(duplicates)
        # @lc code=end
