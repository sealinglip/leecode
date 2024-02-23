#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-12 16:35:22
LastEditors: Thomas Young
LastEditTime: 2020-09-29 09:17:18
'''
#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# 给定一个二叉树，返回它的 后序 遍历。

# 示例:
# 输入: [1, null, 2, 3]
#   1
#    \
#     2
#    /
#   3

# 输出: [3, 2, 1]
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        # 方法1：递归
        # def postOrder(node: TreeNode, arr: List):
        #     if node.left:
        #         postOrder(node.left, arr)
        #     if node.right:
        #         postOrder(node.right, arr)
        #     arr.append(node.val)
        # postOrder(root, res)
        
        # 方法2：迭代
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     res.append(node.val)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        
        # res.reverse() #这个很重要，翻转后返回

        # 方法3：迭代（不翻转）
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.right is None or prev == root.right:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return res

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.postorderTraversal(TreeNode.createBFSTree([1, None, 2, 3]))) # [3, 2, 1]
    print(solution.postorderTraversal(TreeNode.createBFSTree([1, None, 2, 3, 4]))) # [3, 4, 2, 1]