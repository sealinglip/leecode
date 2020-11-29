#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-29 08:29:02
LastEditors: Thomas Young
LastEditTime: 2020-10-29 08:48:36
'''
#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#
# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

# 例如，从根到叶子节点路径 1 -> 2 -> 3 代表数字 123。
# 计算从根到叶子节点生成的所有数字之和。
# 说明: 叶子节点是指没有子节点的节点。

# 示例 1:
# 输入: [1, 2, 3]
#     1
#    / \
#   2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.

# 示例 2:
# 输入: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026.

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        sum = 0
        stack = [(root, 0)]  # 记录从根到当前节点的路径
        while stack:
            node, flag = stack.pop()
            if flag == 0: # 左子树尚未遍历
                flag = 1
                if node.left:
                    stack.append((node, flag))  # 重新压入
                    stack.append((node.left, 0))
                    continue
            if flag == 1: # 右子树尚未遍历
                flag = 2
                if node.right:
                    stack.append((node, flag))  # 重新压入
                    stack.append((node.right, 0))
                    continue
            if flag ==2:
                if not node.left and not node.right: # 🍃节点
                    sum += int("".join([str(n.val) for n,
                                        f in stack]) + str(node.val))
                
        return sum

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.sumNumbers(TreeNode.createBFSTree([1])))
    print(solution.sumNumbers(TreeNode.createBFSTree([1, 2, 3])))
    print(solution.sumNumbers(TreeNode.createBFSTree([4, 9, 0, 5, 1])))
