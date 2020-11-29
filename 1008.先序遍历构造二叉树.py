#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-07-03 23:09:17
@LastEditors: Thomas Young
@LastEditTime: 2020-07-03 23:10:38
'''
#
# @lc app=leetcode.cn id=1008 lang=python3
#
# [1008] 先序遍历构造二叉树
#
# 返回与给定先序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。
# (回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于 node.left 的任何后代，值总 < node.val，而 node.right 的任何后代，值总 > node.val。此外，先序遍历首先显示节点的值，然后遍历 node.left，接着遍历 node.right。）

#  示例：
#  输入：[8, 5, 1, 7, 10, 12]
#  输出：[8, 5, 10, 1, 7, null, 12]
#  提示：
#  1 <= preorder.length <= 100
#  先序 preorder 中的值是不同的。

from treenode import TreeNode
from typing import List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
# @lc code=end

