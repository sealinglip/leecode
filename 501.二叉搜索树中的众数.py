#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-24 08:09:59
LastEditors: Thomas Young
LastEditTime: 2020-09-24 09:48:34
'''
#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#
# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

# 假定 BST 有如下定义：

# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树
# 例如：
# 给定 BST[1, null, 2, 2],

#   1
#     \
#      2
#     /
#    2
# 返回[2].

# 提示：如果众数超过1个，不需考虑输出顺序
# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

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
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        maxCount, curCount, preVal = 0, 0, None

        def inOrder(node: TreeNode):
            if node.left:
                inOrder(node.left)

            nonlocal preVal, maxCount, curCount  
            if preVal == node.val:
                curCount += 1
            else:
                curCount = 1
                preVal = node.val

            if curCount >= maxCount:
                if curCount > maxCount:
                    res.clear()
                    maxCount = curCount
                res.append(preVal)

            if node.right:
                inOrder(node.right)

        inOrder(root)
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMode(TreeNode.createBFSTree([1, None, 2, 2])))
