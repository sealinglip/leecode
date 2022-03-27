#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#
# 给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。


# 示例 1：
# 输入: root = [5, 3, 6, 2, 4, null, 7], k = 9
# 输出: true

# 示例 2：
# 输入: root = [5, 3, 6, 2, 4, null, 7], k = 28
# 输出: false


# 提示:
# 二叉树的节点个数的范围是[1, 10^4].
# -10 ^ 4 <= Node.val <= 10 ^ 4
# root 为二叉搜索树
# -10 ^ 5 <= k <= 10 ^ 5


from treenode import TreeNode
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        visted = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if k - node.val in visted:
                return True
            visted.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False
        # @lc code=end
