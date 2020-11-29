#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-12 16:30:25
LastEditors: Thomas Young
LastEditTime: 2020-10-27 08:22:14
'''
#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# 给定一个二叉树，返回它的 前序 遍历。

# 示例:

# 输入: [1, null, 2, 3]
#    1
#     \
#      2
#     /
#    3

# 输出: [1, 2, 3]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 通过利用栈来递归遍历
        res = []
        if not root:
            return res
            
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return res
# @lc code=end

