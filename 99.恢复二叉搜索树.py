#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-07-05 20:41:05
@LastEditors: Thomas Young
@LastEditTime: 2020-07-07 07:57:33
'''
#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#
# 二叉搜索树中的两个节点被错误地交换。

# 请在不改变其结构的情况下，恢复这棵树。

# 示例 1:
# 输入: [1, 3, null, null, 2]
#    1
#   /
#  3
#   \
#    2
# 输出: [3,1,null,null,2]
#    3
#   /
#  1
#   \
#    2

# 示例 2:
# 输入: [3,1,4,null,null,2]
#   3
#  / \
# 1   4
#    /
#   2
# 输出: [2,1,4,null,null,3]
#   2
#  / \
# 1   4
#    /
#   3

# 进阶:
# 使用 O(n) 空间复杂度的解法很容易实现。
# 你能想出一个只使用常数空间的解决方案吗？

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
from typing import List
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preNode, node1, node2 = None, None, None
        # 1. 中序遍历树
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if preNode and node.val < preNode.val:
                    node2 = node
                    if not node1:
                        node1 = preNode
                    else:
                        break
                preNode = node
                node = node.right

        # 2. Morris 中序遍历

        if node1 and node2:
            node1.val, node2.val = node2.val, node1.val
        return

# @lc code=end
if __name__ == "__main__":
    solution = Solution()

    root = TreeNode.createBFSTree([0, 1])
    solution.recoverTree(root)
    print(root.serialize())

    root = TreeNode.createBFSTree([2, 3, 1])
    solution.recoverTree(root)
    print(root.serialize())

    root = TreeNode.createPreOrderTree([3, None, 2, None, 1])
    solution.recoverTree(root)
    print(root.serialize())
