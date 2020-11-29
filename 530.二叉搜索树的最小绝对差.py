#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-12 08:40:33
LastEditors: Thomas Young
LastEditTime: 2020-10-12 08:55:10
'''
#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

# 示例：
# 输入：

#   1
#    \
#     3
#    /
#   2
# 输出：
# 1

# 解释：
# 最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。

# 提示：
# 树中至少有 2 个节点。
# 本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes / 相同

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        valSet = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val in valSet:
                return 0
            else:
                valSet.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        vals = list(valSet)
        vals.sort()
        prev = float("inf")
        delta = prev
        for val in vals:
            newDelta = abs(val - prev)
            if newDelta < delta:
                delta = newDelta
            prev = val
        
        return delta

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.getMinimumDifference(TreeNode.createBFSTree([1, None, 3, 2])))