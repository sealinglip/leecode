#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-06 08:57:53
LastEditors: Thomas Young
LastEditTime: 2020-09-06 09:16:35
'''
#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# 给定一个二叉树，找出其最大深度。

# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。

# 示例：
# 给定二叉树[3, 9, 20, null, null, 15, 7]，
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        maxDepth = 1
        while stack:
            node, depth = stack.pop()
            if depth > maxDepth:
                maxDepth = depth
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        
        return maxDepth
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDepth(TreeNode.createBFSTree(
        [3, 9, 20, None, None, 15, 7])))
