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
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。


# 示例 1:
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]

# 示例 2:
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
 

# 提示:
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder 和 inorder 均 无重复 元素
# inorder 均出现在 preorder
# preorder 保证 为二叉树的前序遍历序列
# inorder 保证 为二叉树的中序遍历序列

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

if __name__ == "__main__":
    solution = Solution()
    print(solution.buildTree([3,9,20,15,7], [9,3,15,20,7]).serialize()) # [3,9,20,None,None,15,7]
    print(solution.buildTree([-1], [-1]).serialize()) # [-1]