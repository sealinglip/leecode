#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-19 23:07:12
LastEditors: Thomas Young
LastEditTime: 2020-09-19 23:13:49
'''
#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# 计算给定二叉树的所有左叶子之和。

# 示例：
#     3
#    / \
#   9  20
#     /  \
#    15   7

# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        sum = 0
        def addLeftLeave(node: TreeNode, left: bool):
            if left and not node.left and not node.right:
                nonlocal sum
                sum += node.val
            else:
                if node.left:
                    addLeftLeave(node.left, True)
                if node.right:
                    addLeftLeave(node.right, False)

        addLeftLeave(root, False)         
        return sum
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOfLeftLeaves(TreeNode.createBFSTree([3, 9, 20, None, None, 15, 7])))