#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-12 06:53:47
LastEditors: Thomas Young
LastEditTime: 2020-09-12 07:02:31
'''
#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#
# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

# 示例 1：
# 输入：
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 输出：[3, 14.5, 11]
# 解释：
# 第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。

# 提示：
# 节点值的范围在32位有符号整数范围内。

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
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return None

        lvl = [root]
        avg = []
        while lvl:
            nextLvl = []
            size = len(lvl)
            sum = 0
            for node in lvl:
                sum += node.val
                if node.left:
                    nextLvl.append(node.left)
                if node.right:
                    nextLvl.append(node.right)
            avg.append(sum / size)
            lvl = nextLvl
            
        return avg
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.averageOfLevels(TreeNode.createBFSTree([3, 9, 20, None, None, 15, 7])))