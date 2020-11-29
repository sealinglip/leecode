#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-04 08:26:39
LastEditors: Thomas Young
LastEditTime: 2020-09-04 08:36:42
'''
#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 说明: 叶子节点是指没有子节点的节点。

# 示例:
# 输入:
#    1
#  /   \
# 2     3
#  \
#   5
# 输出: ["1->2->5", "1->3"]

# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        res = []
        stack = []
        
        def dfs(node: TreeNode):
            stack.append(node)
            if not node.left and not node.right:
                res.append("->".join([str(n.val) for n in stack]))
            else:
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
            stack.pop()

        dfs(root)
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.binaryTreePaths(TreeNode.createBFSTree(
        [10, 5, 15, None, None, 6, 20])))
