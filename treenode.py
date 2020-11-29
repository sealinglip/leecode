#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-12 20:50:01
LastEditors: Thomas Young
LastEditTime: 2020-09-27 08:19:04
'''
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # BFS遍历树解法
    def serialize(self) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        stack = deque()
        stack.append(self)  # 根节点
        valList = []
        while stack:
            node = stack.popleft()
            valList.append(str(node.val) if node else 'N')
            if node:
                stack.extend([node.left, node.right])

        return ','.join(valList)

    @staticmethod
    def createBFSTree(arr):
        """
        arr 广度优先遍历节点列表
        """
        if not arr:
            return None
        nodeList = []
        for v in arr:
            nodeList.append(TreeNode(v) if v != None else None)

        depth = [nodeList[0]] # 逐层构建
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

    @staticmethod
    def createPreOrderTree(arr):
        """
        arr 二叉树前序遍历节点列表
        """
        stack = []
        preNull = False
        root = None
        for num in arr:
            if num is None: # 空
                if preNull:
                    stack.pop()
                preNull = True
            else:
                node = TreeNode(num)
                if not root:
                    root = node
                if preNull:
                    parent = stack.pop()
                    parent.right = node
                elif stack:
                    parent = stack[-1]
                    parent.left = node
                preNull = False
                stack.append(node)

        return root


if __name__ == "__main__":
    # node = TreeNode.createBFSTree([5, 1, 4, None, None, 3, 6])
    # print(node.val)
    node = TreeNode.createPreOrderTree([1, None, 2, 3])
    print(node.val)
