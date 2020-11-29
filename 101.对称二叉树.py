#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-08-28 07:39:49
LastEditors: Thomas Young
LastEditTime: 2020-08-28 23:14:49
'''
#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# 给定一个二叉树，检查它是否是镜像对称的。

# 例如，二叉树[1, 2, 2, 3, 4, 4, 3] 是对称的。
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
 

# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#     1
#    / \
#   2   2
#    \   \
#    3    3
 

# 进阶：

# 你可以运用递归和迭代两种方法解决这个问题吗？

from treenode import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        # 递归
        # def isMirror(n1: TreeNode, n2: TreeNode) -> bool:
        #     if n1 is None or n2 is None:
        #         return n1 == n2
        #     elif n1.val != n2.val:
        #         return False
        #     else:
        #         return isMirror(n1.left, n2.right) and isMirror(n1.right, n2.left)
        # return isMirror(root.left, root.right)

        # 迭代
        # 层序遍历
        queue = [root]
        symmetric = True
        while queue:
            value = [n.val if n else None for n in queue]
            if value != value[::-1]:  # 不对称的话
                symmetric = False
                break
            nextLevel = []
            for n in queue:
                if n:
                    nextLevel.append(n.left)
                    nextLevel.append(n.right)
            queue = nextLevel

        return symmetric

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.isSymmetric(TreeNode.createBFSTree([1, 2, 2, 3, 4, 4, 3])))
    print(solution.isSymmetric(
        TreeNode.createBFSTree([1, 2, 2, None, 3, None, 3])))
