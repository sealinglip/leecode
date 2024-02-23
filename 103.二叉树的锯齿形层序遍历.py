#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-18 08:01:32
LastEditors: Thomas Young
LastEditTime: 2020-10-18 08:08:31
'''
#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

# 示例 1：
# 给定二叉树[3, 9, 20, null, null, 15, 7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回锯齿形层次遍历如下：
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# 示例 2：
# 输入：root = [1]
# 输出：[[1]]

# 示例 3：
# 输入：root = []
# 输出：[]
 

# 提示：
# 树中节点数目在范围 [0, 2000] 内
# -100 <= Node.val <= 100

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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        lvl = [root]
        reverse = True
        while lvl:
            res.append([n.val for n in lvl])
            newLvl = []
            if reverse:
                for n in lvl:
                    if n.left:
                        newLvl.append(n.left)
                    if n.right:
                        newLvl.append(n.right)
            else:
                for n in lvl:
                    if n.right:
                        newLvl.append(n.right)
                    if n.left:
                        newLvl.append(n.left)
                    
            reverse = not reverse
            newLvl.reverse()
            lvl = newLvl

        return res

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.zigzagLevelOrder(TreeNode.createBFSTree([3, 9, 20, None, None, 15, 7]))) # [[3],[20,9],[15,7]]
    print(solution.zigzagLevelOrder(TreeNode.createBFSTree([1]))) # [[1]]
    print(solution.zigzagLevelOrder(TreeNode.createBFSTree([]))) # []
