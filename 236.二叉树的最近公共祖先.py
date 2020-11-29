#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-27 08:52:25
LastEditors: Thomas Young
LastEditTime: 2020-09-27 08:57:13
'''
#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
# 满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# 例如，给定如下二叉树:  root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]

# 示例 1:
# 输入: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

# 示例 2:
# 输入: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

# 说明:
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。

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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None

        pathP = []
        pathQ = []

        def dfs(node: 'TreeNode', path: 'List', target: 'TreeNode') -> bool:
            path.append(node)
            if node == target:
                return True
            if node.left:
                if dfs(node.left, path, target):
                    return True
            if node.right:
                if dfs(node.right, path, target):
                    return True
            path.pop()
            return False

        dfs(root, pathP, p)
        dfs(root, pathQ, q)

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
    root = TreeNode.createBFSTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    solution = Solution()
    commonAncestor = solution.lowestCommonAncestor(root, root.left, root.right)
    print(commonAncestor.val if commonAncestor else -1)
    commonAncestor = solution.lowestCommonAncestor(
        root, root.left, root.left.right.right)
    print(commonAncestor.val if commonAncestor else -1)
