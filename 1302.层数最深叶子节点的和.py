#
# @lc app=leetcode.cn id=1302 lang=python3
#
# [1302] 层数最深叶子节点的和
#
# 给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。


# 示例 1：
# 输入：root = [1, 2, 3, 4, 5, null, 6, 7, null, null, null, null, 8]
# 输出：15

# 示例 2：
# 输入：root = [6, 7, 8, 2, 7, 1, 3, 9, null, 1, 4, null, null, null, 5]
# 输出：19


# 提示：
# 树中节点数目在范围[1, 10^4] 之间。
# 1 <= Node.val <= 100

from typing import Optional
from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        lvl = [root]
        while lvl:
            newLvl = []
            for n in lvl:
                if n.left:
                    newLvl.append(n.left)
                if n.right:
                    newLvl.append(n.right)
            if not newLvl:
                break
            lvl = newLvl
        return sum([n.val for n in lvl], 0)

# @lc code=end
