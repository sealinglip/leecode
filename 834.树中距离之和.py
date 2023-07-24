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
# 给定一个无向、连通的树。树中有 n 个标记为 0...n-1 的节点以及 n-1 条边 。
# 给定整数 n 和数组 edges ， edges[i] = [ai, bi]表示树中的节点 ai 和 bi 之间有一条边。
# 返回长度为 n 的数组 answer ，其中 answer[i] 是树中第 i 个节点与所有其他节点之间的距离之和。

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

# 示例 2:
# 输入: n = 1, edges = []
# 输出: [0]

# 示例 3:
# 输入: n = 2, edges = [[1, 0]]
# 输出: [1, 1]

# 提示:
# 1 <= n <= 3 * 10^4
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# 给定的输入保证为有效的树

# Hard

from typing import List
# @lc code=start


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        if not n:
            return []

        # 先记录每个节点的连通情况
        tree = [[] for _ in range(n)]
        for n1, n2 in edges:
            tree[n1].append(n2)
            tree[n2].append(n1)
        depth = [0 for _ in range(n)]  # 存储以每个节点在以0节点为根时的树深度
        count = [0 for _ in range(n)]  # 每个节点的子节点数量(含自身)

        def dfsForDepthAndCount(node: int, parent: int):
            count[node] = 1
            for link in tree[node]:
                if link != parent:  # 不走来时路
                    depth[link] = depth[node] + 1
                    dfsForDepthAndCount(link, node)
                    count[node] += count[link]

        dfsForDepthAndCount(0, -1)

        answer = [0 for _ in range(n)]
        answer[0] = sum(depth)

        def dfsForAnswer(node: int, parent: int):
            for link in tree[node]:
                if link != parent:
                    # 当出发点从node转移到link时，link下所有子节点（含自身）距离都缩短了1，而其他所有节点距离都增加了1
                    # answer[link] = answer[node] - count[link] + (n - count[link])
                    answer[link] = answer[node] - 2 * count[link] + n
                    dfsForAnswer(link, node)

        dfsForAnswer(0, -1)

        return answer


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOfDistancesInTree(
        1, []))  # [0]
    print(solution.sumOfDistancesInTree(
        6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))  # [8,12,6,10,10,10]
