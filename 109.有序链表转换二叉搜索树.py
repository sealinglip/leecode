#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-07-03 14:40:37
@LastEditors: Thomas Young
@LastEditTime: 2020-07-03 15:05:05
'''
#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#
# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

# 示例:
# 给定的有序链表： [-10, -3, 0, 5, 9],
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

from treenode import TreeNode
from listnode import ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        len = 0 # 求链表长度
        node = head
        while node:
            len += 1
            node = node.next
        
        def buildBST(lb: int, ub: int) -> TreeNode:
            '''
            按中序遍历节点列表构造数
            '''
            if lb > ub:
                return None

            mid = (lb + ub) >> 1
            left = buildBST(lb, mid - 1)
            nonlocal head
            node = TreeNode(head.val)
            head = head.next
            right = buildBST(mid + 1, ub)
            
            node.left = left
            node.right = right
            return node

        return buildBST(0, len - 1)
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    solution.sortedListToBST(ListNode.convert_list([-10, -3, 0, 5, 9]))
