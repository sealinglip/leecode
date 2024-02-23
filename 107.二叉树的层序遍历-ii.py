#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-06 09:11:37
LastEditors: Thomas Young
LastEditTime: 2020-09-06 09:17:31
'''
#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

# 例如：
# 给定二叉树[3, 9, 20, null, null, 15, 7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其自底向上的层次遍历为：

# [
#   [15,7],
#   [9,20],
#   [3]
# ]

from typing import List
from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        nodes = [[root]]
        while True:
            level = []
            for n in nodes[-1]:
                if n.left:
                    level.append(n.left)
                if n.right:
                    level.append(n.right)
                
            if level:
                nodes.append(level)
            else:
                break

        return [[n.val for n in level] for level in nodes][::-1]
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.levelOrderBottom(TreeNode.createBFSTree(
        [3, 9, 20, None, None, 15, 7])))
