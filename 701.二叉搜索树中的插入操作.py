#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-30 08:43:00
LastEditors: Thomas Young
LastEditTime: 2020-09-30 08:57:10
'''
#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
# 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 
# 输入数据保证，新值和原始二叉搜索树中的任意节点值都不同。

# 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。

# 例如,
# 给定二叉搜索树:
#         4
#        / \
#       2   7
#      / \
#     1   3
# 和 插入的值: 5
# 你可以返回这个二叉搜索树:
#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5
# 或者这个树也是有效的:
#          5
#        /   \
#       2     7
#      / \   
#     1   3
#          \
#           4
 

# 提示：

# 给定的树上的节点数介于 0 和 10^4 之间
# 每个节点都有一个唯一整数值，取值范围从 0 到 10^8
# -10^8 <= val <= 10^8
# 新值和原始二叉搜索树中的任意节点值都不同

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        node = root
        prev = None
        dir = 0
        while node:
            prev = node
            if node.val > val:
                node = node.left
                dir = 0
            elif node.val < val:
                node = node.right
                dir = 1
        
        if dir:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)
            
        return root
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode.createBFSTree([4, 2, 7, 1, 3])
    solution.insertIntoBST(root, 5)
    print(root.serialize())
