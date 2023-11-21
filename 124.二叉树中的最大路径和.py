#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-21 11:01:54
@LastEditors: Thomas Young
@LastEditTime: 2020-06-21 16:21:18
'''
#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

# 路径和 是路径中各节点值的总和。

# 给你一个二叉树的根节点 root ，返回其 最大路径和 。


# 示例 1：
# 输入：root = [1, 2, 3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

# 示例 2：
# 输入：root = [-10, 9, 20, null, null, 15, 7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42


# 提示：
# 树中节点数目范围是[1, 3 * 10^4]
# -1000 <= Node.val <= 1000

# Hard

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import Dict


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        # 每个节点都计算一个值，即以它为起点，伸出一臂向子节点走，最大的路径和
        # max_path(node) = node.val + max(0, max_path(node.left), max_path(node.right))
        # 对于🍃节点，max_path(node) = node.val
        # maxPathSum = max(node.val + max(0, max_path(node.left)) + max(0, max_path(node.right)), ……)
        maxPathSum = float('-inf')

        def get_max_path(node: TreeNode) -> int:
            if not node:
                return 0
            max_left = max(0, get_max_path(node.left))
            max_right = max(0, get_max_path(node.right))

            nonlocal maxPathSum
            curPathSum = node.val + max_left + max_right
            if curPathSum > maxPathSum:
                maxPathSum = curPathSum
            return node.val + max(max_left, max_right)

        # 遍历🌲节点，求max_path最值
        get_max_path(root)

        return maxPathSum

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    node = TreeNode.createBFSTree([-3])
    print(solution.maxPathSum(node))
    node = TreeNode.createBFSTree([1, 2, 3])
    print(solution.maxPathSum(node))
    node = TreeNode.createBFSTree([-10, 9, 20, None, None, 15, 7])
    print(solution.maxPathSum(node))
