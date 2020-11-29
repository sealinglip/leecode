#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-08 22:06:32
LastEditors: Thomas Young
LastEditTime: 2020-09-08 22:19:33
'''
#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。

# 本题中，一棵高度平衡二叉树定义为：
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

# 示例 1:
# 给定二叉树[3, 9, 20, None, None, 15, 7]
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。

# 示例 2:
# 给定二叉树 [1,2,2,3,3,None,None,4,4]
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def getBalancedDepth(node: TreeNode) -> int:
            """如果是平衡二叉🌲，返回🌲的深度；否则返回-1

            Args:
                node (TreeNode): 根节点

            Returns:
                int: 🌲深度
            """
            leftDepth = getBalancedDepth(node.left) if node.left else 0
            if leftDepth == -1:
                return -1
                
            rightDepth = getBalancedDepth(node.right) if node.right else 0
            if rightDepth == -1:
                return -1
            
            return max(leftDepth, rightDepth) + 1 if abs(leftDepth - rightDepth) < 2 else -1

        return getBalancedDepth(root) != -1
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.isBalanced(
        TreeNode.createBFSTree([3, 9, 20, None, None, 15, 7])))
    print(solution.isBalanced(TreeNode.createBFSTree(
        [1, 2, 2, 3, 3, None, None, 4, 4])))
