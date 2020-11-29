#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-06 07:49:08
LastEditors: Thomas Young
LastEditTime: 2020-10-08 22:11:57
'''
#
# @lc app=leetcode.cn id=834 lang=python3
#
# [834] 树中距离之和
#
# 给定一个无向、连通的树。树中有 N 个标记为 0...N-1 的节点以及 N-1 条边 。
# 第 i 条边连接节点 edges[i][0] 和 edges[i][1] 。
# 返回一个表示节点 i 与其他所有节点距离之和的列表 ans。

# 示例 1:
# 输入: N = 6, edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
# 输出: [8, 12, 6, 10, 10, 10]
# 解释:
# 如下为给定的树的示意图：
#   0
#  / \
# 1   2
#    /|\
#   3 4 5
# 我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5) 
# 也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。
# 说明: 1 <= N <= 10000

from typing import List
# @lc code=start
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        if not N:
            return []
        
        # 先记录每个节点的连通情况
        tree = [[] for _ in range(N)]
        for n1, n2 in edges:
            tree[n1].append(n2)
            tree[n2].append(n1)
        depth = [0 for _ in range(N)] # 存储以每个节点在以0节点为根时的树深度
        count = [0 for _ in range(N)] # 每个节点的子节点数量(含自身)

        def dfsForDepthAndCount(node: int, parent: int):
            count[node] = 1
            for link in tree[node]:
                if link != parent: # 不走来时路
                    depth[link] = depth[node] + 1
                    dfsForDepthAndCount(link, node)
                    count[node] += count[link]
        
        dfsForDepthAndCount(0, -1)

        answer = [0 for _ in range(N)]
        answer[0] = sum(depth)

        def dfsForAnswer(node: int, parent: int):
            for link in tree[node]:
                if link != parent:
                    # 当出发点从node转移到link时，link下所有子节点（含自身）距离都缩短了1，而其他所有节点距离都增加了1
                    # answer[link] = answer[node] - count[link] + (N - count[link])
                    answer[link] = answer[node] - 2 * count[link] + N 
                    dfsForAnswer(link, node)

        dfsForAnswer(0, -1)

        return answer

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOfDistancesInTree(
        1, []))
    print(solution.sumOfDistancesInTree(
        6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
