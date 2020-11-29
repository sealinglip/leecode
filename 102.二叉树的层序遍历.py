#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-06 08:51:22
LastEditors: Thomas Young
LastEditTime: 2020-09-06 09:16:20
'''
#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。


# 示例：
# 二叉树：[3, 9, 20, null, null, 15, 7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：

# [
#   [3],
#   [9,20],
#   [15,7]
# ]

from typing import List
from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        nodes = [[root]]
        while True:
            level = []
            for n in nodes[-1]:
                if n.left:
                    level.append(n.left)
                if n.right:
                    level.append(n.right)
                
            if level:
                nodes.append(level)
            else:
                break
        
        return [[n.val for n in level] for level in nodes]

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.levelOrder(
        TreeNode.createBFSTree([3, 9, 20, None, None, 15, 7])))
