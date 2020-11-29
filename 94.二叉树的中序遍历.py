#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-07-03 19:32:20
@LastEditors: Thomas Young
@LastEditTime: 2020-07-05 16:36:36
'''
#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# 给定一个二叉树，返回它的中序 遍历。

# 示例:
# 输入: [1, null, 2, 3]
#    1
#     \
#      2
#     /
#    3

# 输出: [1, 3, 2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        # 1、递归算法
        # def inorder(node: TreeNode):
        #     if node.left:
        #         inorder(node.left)
        #     res.append(node.val)
        #     if node.right:
        #         inorder(node.right)
        # inorder(root)

        # 2、迭代算法
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.inorderTraversal(
        TreeNode.createPreOrderTree([1, None, 2, 3])))
