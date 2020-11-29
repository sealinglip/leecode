#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-16 08:58:37
LastEditors: Thomas Young
LastEditTime: 2020-09-16 09:07:10
'''
#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#
# 翻转一棵二叉树。

# 示例：
# 输入：
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 输出：
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# 备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：
# 谷歌：我们90％的工程师使用您编写的软件(Homebrew)，
# 但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            left = self.invertTree(root.right)
            right = self.invertTree(root.left)
            root.left = left
            root.right = right
        return root
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.invertTree(TreeNode.createBFSTree(
        [4, 2, 7, 1, 3, 6, 9])).serialize())
