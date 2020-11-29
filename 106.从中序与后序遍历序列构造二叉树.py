#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-25 08:02:40
LastEditors: Thomas Young
LastEditTime: 2020-09-25 08:12:50
'''
#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# 根据一棵树的中序遍历与后序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。

# 例如，给出

# 中序遍历 inorder = [9, 3, 15, 20, 7]
# 后序遍历 postorder = [9, 15, 7, 20, 3]
# 返回如下的二叉树：

#     3
#    / \
#   9  20
#     /  \
#    15   7

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        
        l = len(inorder)
        root = TreeNode(postorder[-1])
        # 找到root在inorder的位置
        ri = inorder.index(root.val)
        
        root.left = self.buildTree(inorder[0:ri], postorder[0:ri])
        root.right = self.buildTree(inorder[ri+1:], postorder[ri:l-1])

        return root
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]).serialize())
