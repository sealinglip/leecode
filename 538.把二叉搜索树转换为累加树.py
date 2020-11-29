#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-21 08:39:36
LastEditors: Thomas Young
LastEditTime: 2020-09-21 08:48:06
'''
#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#
# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，
# 使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

# 例如：

# 输入: 原始二叉搜索树:
#               5
#             /   \
#            2     13

# 输出: 转换为累加树:
#              18
#             /   \
#           20     13

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            stack = [] # 中序遍历，所有节点入栈
            def midorder(node: TreeNode):
                if node.left:
                    midorder(node.left)
                stack.append(node)
                if node.right:
                    midorder(node.right)
            
            midorder(root)
            sum = 0
            while stack:
                node = stack.pop()
                node.val += sum
                sum = node.val
                
        return root
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    root = solution.convertBST(TreeNode.createBFSTree([5, 2, 13]))
    print(root.serialize())
