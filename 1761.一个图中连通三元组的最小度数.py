#
# @lc app=leetcode.cn id=1761 lang=python3
#
# [1761] 一个图中连通三元组的最小度数
#
# 给你一个无向图，整数 n 表示图中节点的数目，edges 数组表示图中的边，其中 edges[i] = [ui, vi] ，表示 ui 和 vi 之间有一条无向边。

# 一个 连通三元组 指的是 三个 节点组成的集合且这三个点之间 两两 有边。

# 连通三元组的度数 是所有满足此条件的边的数目：一个顶点在这个三元组内，而另一个顶点不在这个三元组内。

# 请你返回所有连通三元组中度数的 最小值 ，如果图中没有连通三元组，那么返回 - 1 。


# 示例 1：
# 输入：n = 6, edges = [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]
# 输出：3
# 解释：只有一个三元组[1, 2, 3] 。构成度数的边在上图中已被加粗。

# 示例 2：
# 输入：n = 7, edges = [[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]]
# 输出：0
# 解释：有 3 个三元组：
# 1)[1, 4, 3]，度数为 0 。
# 2)[2, 5, 6]，度数为 2 。
# 3)[5, 6, 7]，度数为 2 。


# 提示：
# 2 <= n <= 400
# edges[i].length == 2
# 1 <= edges.length <= n * (n-1) / 2
# 1 <= ui, vi <= n
# ui != vi
# 图中没有重复的边。

# Hard

from collections import defaultdict
from math import inf
from typing import List
# @lc code=start


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # 记录所有点关联的点
        graph = defaultdict(set)  # 无向图
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # 转成有向图，好遍历
        digraph = defaultdict(list)  # 有向图
        for u, v in edges:
            u_d, v_d = len(graph[u]), len(graph[v])
            if u_d < v_d or (u_d == v_d and u < v):
                digraph[u].append(v)
            else:
                digraph[v].append(u)

        res = inf  # 记录最小度数
        # 枚举三元组
        for i, nodes in digraph.items():
            for j in nodes:
                if j in digraph:
                    for k in digraph[j]:
                        if i in graph[k]:  # 发现三元组
                            res = min(
                                res, len(graph[i]) + len(graph[j]) + len(graph[k]) - 6)

        return -1 if res == inf else res


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minTrioDegree(
        6, [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]))  # 3
    print(solution.minTrioDegree(
        7, [[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]]))  # 0
