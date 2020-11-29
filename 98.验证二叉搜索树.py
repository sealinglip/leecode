#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-12 21:41:37
@LastEditors: Thomas Young
@LastEditTime: 2020-07-05 19:17:06
'''
#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。

# 假设一个二叉搜索树具有如下特征：

# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# 示例 1:
# 输入:
#     2
#    / \
#   1   3
# 输出: true

# 示例 2:
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#
from treenode import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        if root.left:
            if not self.treeValueLimit(root.left, -sys.maxsize - 1, root.val):
                return False
        if root.right:
            if not self.treeValueLimit(root.right, root.val, sys.maxsize):
                return False
        
        return True

    def treeValueLimit(self, root: TreeNode, lb:int, ub: int) -> bool:
        if root.val >= ub or root.val <= lb:
            return False

        if root.left:
            if not self.treeValueLimit(root.left, lb, root.val):
                return False
        if root.right:
            if not self.treeValueLimit(root.right, root.val, ub):
                return False
        return True
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValidBST(TreeNode.createBFSTree(
        [10, 5, 15, None, None, 6, 20])))
