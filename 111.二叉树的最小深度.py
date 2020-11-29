#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-25 08:13:48
LastEditors: Thomas Young
LastEditTime: 2020-09-25 08:22:47
'''
#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# 给定一个二叉树，找出其最小深度。

# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

# 说明: 叶子节点是指没有子节点的节点。

# 示例:
# 给定二叉树[3, 9, 20, null, null, 15, 7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最小深度  2.

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left and right:
            return 1 + min(left, right)
        else:
            return 1 + left + right
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minDepth(TreeNode.createBFSTree(
        [3, 9, 20, None, None, 15, 7])))
