#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-24 09:02:01
LastEditors: Thomas Young
LastEditTime: 2020-11-25 09:36:11
'''
#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#
# 给出一个完全二叉树，求出该树的节点个数。

# 说明：

# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
# 并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

# 示例:

# 输入:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6

# 输出: 6

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # 方法1：递归
        # 缺点：没有利用完全二叉树的特性
        # return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        # 方法2：利用完全二叉树特性的递归
        def depth(node: TreeNode) -> int:
            d = 0
            while node:
                d += 1
                node = node.left
            return d
        
        leftDepth = depth(root.left)
        rightDepth = depth(root.right)
        if leftDepth == rightDepth:
            return self.countNodes(root.right) + (1 << leftDepth)
        else:
            return self.countNodes(root.left) + (1 << rightDepth)


        # 方法3：折半查找：
        # 先求树深度
        # depth = 0
        # node = root
        # while node:
        #     depth += 1
        #     node = node.left
        # # 根据完全二叉树特性，该树节点数为[2^(depth-1), 2^depth-1]
        # # 通过二分法（折半查找）确定节点数
        # def exists(nodeIndex: int) -> bool:
        #     """判断 第nodeIndex 个节点存不存在
        #     如何判断第 k 个节点是否存在呢？如果第 k 个节点位于第 h 层，则 k 的二进制表示包含 h+1 位，
        #     其中最高位是 1，其余各位从高到低表示从根节点到第 k 个节点的路径，0 表示移动到左子节点，1 
        #     表示移动到右子节点。通过位运算得到第 k 个节点对应的路径，判断该路径对应的节点是否存在，即可
        #     判断第 k 个节点是否存在。

        #     Args:
        #         nodeIndex (int): 节点索引

        #     Returns:
        #         bool: 存在与否
        #     """
        #     n = root
        #     bit = 1 << (depth - 2)
        #     while n and bit > 0:
        #         if bit & nodeIndex == 0:
        #             n = n.left
        #         else:
        #             n = n.right
        #         bit >>= 1
        #     return n is not None

        # low, high = 1 << (depth - 1), (1 << depth) - 1
        # while low < high:
        #     mid = (high + low + 1) >> 1
        #     if exists(mid):
        #         low = mid
        #     else:
        #         high = mid - 1
        # return low

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countNodes(TreeNode.createBFSTree([1, 2, 3, 4, 5, 6])))
