#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-22 08:54:13
LastEditors: Thomas Young
LastEditTime: 2020-09-22 23:55:04
'''
#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
#
# 给定一个二叉树，我们在树的节点上安装摄像头。
# 节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
# 计算监控树的所有节点所需的最小摄像头数量。

# 示例 1：
#        0
#       /
#    Camera
#     /  \
#    0    0
# 输入：[0, 0, None, 0, 0]
# 输出：1
# 解释：如图所示，一台摄像头足以监控所有节点。

# 示例 2：
#         0
#        /
#     Camera
#      /
#     0
#    /
# Camera
#     \
#      0
# 输入：[0, 0, None, 0, None, 0, None, None, 0]
# 输出：2
# 解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。

# 提示：

# 给定树的节点数的范围是[1, 1000]。
# 每个节点的值都是 0。

# Hard

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        if not root:
            return 0

        # 方法1：DP
        # 遍历🌲，在遍历的过程中将节点的值改为以本节点为根的子树所需的最小监控摄像头数
        # DP 状态转移方程，定义getMinCC(node)为最小监控摄像头数
        # getMinCC(node) = 0 if node is None
        #                = 1 if isLeaf(node) # 🍃节点
        #                = 1 if isLeaf(node.left) and isLeaf(node.right)
        #                = min(minCC(node, True), minCC(node, False))
        # def isLeaf(node: TreeNode) -> bool:
        #     return node is None or (node.left is None and node.right is None)

        # def minCC(node: TreeNode, setSelf: bool) -> int:
        #     """最少监控摄像头数

        #     Args:
        #         node (TreeNode): 根节点
        #         setSelf (bool): 根节点自己放不放摄像头

        #     Returns:
        #         int: 最少监控摄像头数
        #     """
        #     if setSelf:
        #         cc = 1
        #         if node.left and not isLeaf(node.left):
        #             minLeft = min(getMinCC(node.left), getMinCC(node.left.left) + getMinCC(node.left.right))
        #             cc += minLeft
        #         if node.right and not isLeaf(node.right):
        #             minRight = min(getMinCC(node.right), getMinCC(node.right.left) + getMinCC(node.right.right))
        #             cc += minRight
        #         return cc
        #     else:
        #         cc = 0  # 左节点和右节点必须有一个要放置摄像头
        #         if node.left is None:
        #             cc += minCC(node.right, True)
        #         elif node.right is None:
        #             cc += minCC(node.left, True)
        #         else:
        #             cc = min(minCC(node.left, True) + getMinCC(node.right),
        #                         getMinCC(node.left) + minCC(node.right, True))
        #         return cc

        # def getMinCC(node: TreeNode) -> int:
        #     if not node:
        #         return 0
        #     elif not node.val: # 尚未计算过
        #         if isLeaf(node) or (isLeaf(node.left) and isLeaf(node.right)):
        #             node.val = 1
        #         else:
        #             node.val = min(minCC(node, True), minCC(node, False))
        #     return node.val

        # return getMinCC(root)

        minRequirement = 0

        def dfs(node: TreeNode) -> int:
            if node is None:
                return -1  # no need
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 0 or right == 0:
                nonlocal minRequirement
                minRequirement += 1
                return 1  # has camera
            elif left == 1 or right == 1:
                return -1  # no need
            return 0  # cover by parent

        if dfs(root) == 0:
            minRequirement += 1
        return minRequirement
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.minCameraCover(TreeNode.createBFSTree(
        [0, 0, None, None, 0, 0, None, None, 0, 0])))
    print(solution.minCameraCover(
        TreeNode.createBFSTree([0, None, 0, 0, 0, None, None, 0, 0])))
    print(solution.minCameraCover(TreeNode.createBFSTree(
        [0, None, 0, None, 0, None, 0, None, 0, 0, 0, None, None, 0, 0])))
    print(solution.minCameraCover(TreeNode.createBFSTree([0, 0, None, 0, 0])))
    print(solution.minCameraCover(TreeNode.createBFSTree(
        [0, 0, None, 0, None, 0, None, None, 0])))
