#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-07-05 19:23:11
@LastEditors: Thomas Young
@LastEditTime: 2020-07-05 20:07:54
'''
#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

# 示例：
# 输入：3
# 输出：
# [
#     [1, null, 3, 2],
#     [3, 2, null, 1],
#     [3, 1, null, null, 2],
#     [2, 1, 3],
#     [1, null, 2, null, 3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []

        def generateSearchTrees(lb: int, ub: int) -> List[TreeNode]:
            '''
            [lb, ub] : 生成搜索树节点范围闭区间
            '''
            trees = []
            if lb > ub:
                trees.append(None)
            elif lb == ub:
                trees.append(TreeNode(lb))
            else:
                for r in range(lb, ub + 1):
                    leftSubTrees = generateSearchTrees(lb, r - 1)
                    rightSubTrees = generateSearchTrees(r + 1, ub)
                    for leftSubTree in leftSubTrees:
                        for rightSubTree in rightSubTrees:
                            root = TreeNode(r)
                            root.left = leftSubTree
                            root.right = rightSubTree
                            trees.append(root)
                    
            return trees

        return generateSearchTrees(1, n)
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()

