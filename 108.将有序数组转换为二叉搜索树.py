#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-07-03 14:18:52
@LastEditors: Thomas Young
@LastEditTime: 2020-07-03 14:40:20
'''
#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

# 示例:
# 给定有序数组: [-10, -3, 0, 5, 9],
# 一个可能的答案是：[0, -3, 9, -10, null, 5]，它可以表示下面这个高度平衡二叉搜索树：
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        def buildBST(nums: List[int], lb: int, ub: int) -> TreeNode:
            if lb > ub:
                return None

            mid = (lb + ub) >> 1
            node = TreeNode(nums[mid])
            node.left = buildBST(nums, lb, mid - 1)
            node.right = buildBST(nums, mid + 1, ub)
            return node

        return buildBST(nums, 0, len(nums) - 1)

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    root = solution.sortedArrayToBST([-10, -3, 0, 5, 9])
    
    
