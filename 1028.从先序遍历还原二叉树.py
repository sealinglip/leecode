#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-18 09:24:18
@LastEditors: Thomas Young
@LastEditTime: 2020-07-03 23:09:06
'''
#
# @lc app=leetcode.cn id=1028 lang=python3
#
# [1028] 从先序遍历还原二叉树
#
# 我们从二叉树的根节点 root 开始进行深度优先搜索。
# 在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。
# 如果节点只有一个子节点，那么保证该子节点为左子节点。
# 给出遍历输出 S，还原树并返回其根节点 root。

from treenode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S:
            return None

        S += '-' # 加一个字符保证最后一个节点也能入栈

        stack = [] # 节点堆栈
        lvl, val = 0, None
        for c in S:
            if c.isdigit():
                if val is None:
                    val = 0
                val = val * 10 + int(c)
            else:
                if val != None: # 节点入栈
                    if stack:
                        top, topLvl = stack[-1]
                        while topLvl >= lvl:
                            stack.pop()
                            top, topLvl = stack[-1]
                        node = TreeNode(val)
                        if top.left:
                            top.right = node
                        else:
                            top.left = node
                        stack.append((node, lvl))
                    else:
                        stack.append((TreeNode(val), lvl))
                    lvl, val = 0, None # 入栈之后重置
                lvl += 1 # 层级加1
        return stack[0][0]
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.recoverFromPreorder('1-2--3--4-5--6--7'))
