#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-07-07 22:16:34
LastEditors: Thomas Young
LastEditTime: 2020-09-26 17:43:01
'''
#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

# 说明: 叶子节点是指没有子节点的节点。
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

from treenode import TreeNode
from typing import List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        stack = []
        def dfs(node: TreeNode, target: int):
            stack.append(node.val)
            target -= node.val
            if not node.left and not node.right and target == 0:
                res.append(stack[:])
            else:
                if node.left:
                    dfs(node.left, target)
                if node.right:
                    dfs(node.right, target)

            stack.pop()

        dfs(root, sum)

        return res

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.pathSum(TreeNode.createBFSTree([-2, None, -3]), -5))
    print(solution.pathSum(TreeNode.createBFSTree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22))