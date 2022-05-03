#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-17 08:37:07
LastEditors: Thomas Young
LastEditTime: 2021-01-13 22:34:27
'''
#
# @lc app=leetcode.cn id=685 lang=python3
#
# [685] 冗余连接 II
#
# 在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。
# 每一个节点只有一个父节点，除了根节点没有父节点。

# 输入一个有向图，该图由一个有着N个节点(节点值不重复1, 2, ..., N) 的树及一条附加的边构成。
# 附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

# 结果图是一个以边组成的二维数组。 每一个边 的元素是一对[u, v]，用以表示有向图中连接顶点 u 和顶点 v 的边，
# 其中 u 是 v 的一个父节点。

# 返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。

# 示例 1:
# 输入: [[1, 2], [1, 3], [2, 3]]
# 输出: [2, 3]
# 解释: 给定的有向图如下:
#   1
#  / \
# v   v
# 2-->3
# 示例 2:

# 输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# 输出: [4,1]
# 解释: 给定的有向图如下:
# 5 <- 1 -> 2
#      ^    |
#      |    v
#      4 <- 3
# 注意:

# 二维数组大小的在3到1000范围内。
# 二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。

# Hard

from typing import List
# @lc code=start
from collections import defaultdict


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return None

        N = len(edges)
        parent = dict()  # 记录每个节点的父
        graph = defaultdict(list)
        duplicateEdge = None
        for edge in edges:
            graph[edge[0]].append(edge[1])
            if edge[1] in parent:  # 已经存在，问题找到，但未知要去掉哪条边
                duplicateEdge = edge
            else:
                parent[edge[1]] = edge[0]
        if duplicateEdge:  # 判断与之冲突的边，是否成环，如果未成环，则返回本边；如果有环，就要破环（本边不在环内），返回冲突边
            nodes = set()
            node = duplicateEdge[1]
            while node:
                nodes.add(node)
                node = parent.get(node, None)
                if node in nodes:
                    return [parent[duplicateEdge[1]], duplicateEdge[1]]
            else:
                return duplicateEdge

        # 找出成环的节点
        def isCyclic(node: int, visitFlag: List[bool], stackFlag: List[bool]) -> bool:
            visitFlag[node] = True
            stackFlag[node] = True  # 模拟节点进栈
            for child in graph[node]:
                if not visitFlag[child]:
                    if isCyclic(child, visitFlag, stackFlag):
                        return True
                elif stackFlag[child]:
                    return True
            stackFlag[node] = False  # 模拟节点出栈
            return False

        visited = [False] * (N + 1)
        recStack = [False] * (N + 1)
        nodesInCircle = set()
        for n in range(1, N + 1):
            if not visited[n]:
                if isCyclic(n, visited, recStack):
                    nodesInCircle.add(n)
                    break

        # 找出成环的最后一条边
        for i in range(N-1, -1, -1):
            edge = edges[i]
            if edge[1] in nodesInCircle:
                return edge

        return None

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.findRedundantDirectedConnection(
        [[2, 1], [3, 1], [4, 2], [1, 4]]))
    print(solution.findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]))
    print(solution.findRedundantDirectedConnection(
        [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]))
