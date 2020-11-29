#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-15 20:46:26
LastEditors: Thomas Young
LastEditTime: 2020-10-15 21:54:28
'''
#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# 给定一个二叉树，原地将它展开为一个单链表。
# 例如，给定二叉树：
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6

# 将其展开为：
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            stack = [root]
            prev = None

            while stack:
                node = stack.pop()
                if prev:
                    prev.right = node
                    prev.left = None
                prev = node
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                    
        return root
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    node = TreeNode.createBFSTree([1, 2, 5, 3, 4, None, 6])
    solution.flatten(node)
    print(node.serialize())
