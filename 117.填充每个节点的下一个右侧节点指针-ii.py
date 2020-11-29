#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-28 08:47:30
LastEditors: Thomas Young
LastEditTime: 2020-09-28 11:31:30
'''
#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#
# 给定一个二叉树
# struct Node {
#     int val;
#     Node * left;
#     Node * right;
#     Node * next; }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

# 初始状态下，所有 next 指针都被设置为 NULL。

# 进阶：
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

# 示例：
# 输入：root = [1, 2, 3, 4, 5, null, 7]
# 输出：[1,  # ,2,3,#,4,5,7,#]
#     解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。

# 提示：

# 树中的节点数小于 6000
# - 100 <= node.val <= 100

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    @staticmethod
    def createBFSTree(arr):
        """
        arr 广度优先遍历节点列表
        """
        if not arr:
            return None
        nodeList = []
        for v in arr:
            nodeList.append(Node(v) if v != None else None)

        depth = [nodeList[0]]  # 逐层构建
        i = 1
        l = len(nodeList)
        while depth and i < l:
            newDepth = []
            for node in depth:
                left = nodeList[i]
                if left:
                    node.left = left
                    newDepth.append(left)
                i += 1

                if i >= l:
                    break

                right = nodeList[i]
                if right:
                    node.right = right
                    newDepth.append(right)
                i += 1

                if i >= l:
                    break

            depth = newDepth

        return nodeList[0]

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            # 方法1
            # lvl = [root]
            # while lvl:
            #     newLvl = []
            #     prevNode = None
            #     for node in lvl:
            #         if prevNode:
            #             prevNode.next = node
            #         prevNode = node
            #         if node.left:
            #             newLvl.append(node.left)
            #         if node.right:
            #             newLvl.append(node.right)
            #     lvl = newLvl

            # 方法2（常数级额外空间）
            start = root
            while start:
                nextStart = None
                node = start
                last = None
                while node:
                    if node.left:
                        if last:
                            last.next = node.left
                        else:
                            nextStart = node.left
                        last = node.left
                    if node.right:
                        if last:
                            last.next = node.right
                        else:
                            nextStart = node.right
                        last = node.right
                    node = node.next
                        
                start = nextStart
        return root
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    root = Node.createBFSTree([1, 2, 3, 4, 5, None, 7])
    root = solution.connect(root)
    
