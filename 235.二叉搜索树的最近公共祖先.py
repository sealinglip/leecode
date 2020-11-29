#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-27 08:03:41
LastEditors: Thomas Young
LastEditTime: 2020-09-27 09:04:33
'''
#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 
# x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# 例如，给定如下二叉搜索树:  root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]

# 示例 1:
# 输入: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
# 输出: 6
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。

# 示例 2:
# 输入: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

# 说明:
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中。

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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None

        pathP = []
        pathQ = []

        # 方法1：递归
        # def dfs(node: 'TreeNode', path: 'List', target: 'TreeNode'):
        #     path.append(node)
        #     if node == target:
        #         return
        #     if node.left and target.val < node.val:
        #         dfs(node.left, path, target)
        #     elif node.right and target.val > node.val:
        #         dfs(node.right, path, target)
        
        # dfs(root, pathP, p)
        # dfs(root, pathQ, q)

        # 方法2：迭代
        def findPath(node: 'TreeNode', path: 'List', target: 'TreeNode'):
            while node:
                path.append(node)
                if node == target:
                    break
                if node.left and target.val < node.val:
                    node = node.left
                elif node.right:
                    node = node.right
        
        findPath(root, pathP, p)
        findPath(root, pathQ, q)

        l = min(len(pathP), len(pathQ))
        lca = None
        for i in range(l):
            if pathP[i] == pathQ[i]:
                lca = pathP[i]
            else:
                break
        
        return lca
        
# @lc code=end

if __name__ == "__main__":
    root = TreeNode.createBFSTree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    solution = Solution()
    commonAncestor = solution.lowestCommonAncestor(root, root.left, root.right)
    print(commonAncestor.val if commonAncestor else -1)
    commonAncestor = solution.lowestCommonAncestor(root, root.left, root.left.right)
    print(commonAncestor.val if commonAncestor else -1)
