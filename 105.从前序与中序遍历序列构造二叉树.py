#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-12 21:00:38
@LastEditors: Thomas Young
@LastEditTime: 2020-06-12 21:05:53
'''
#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        node = TreeNode(preorder[0]) # 根节点
        idxInInorder = 0
        while inorder[idxInInorder] != node.val:
            idxInInorder += 1
        
        node.left = self.buildTree(preorder[1:idxInInorder+1], inorder[0:idxInInorder])
        node.right = self.buildTree(preorder[idxInInorder+1:], inorder[idxInInorder+1:])

        return node

# @lc code=end

