#
# @lc app=leetcode.cn id=1617 lang=python3
#
# [1617] 统计子树中城市之间最大距离
#
# 给你 n 个城市，编号为从 1 到 n 。同时给你一个大小为 n-1 的数组 edges ，其中 edges[i] = [ui, vi] 表示城市 ui 和 vi 之间有一条双向边。
# 题目保证任意城市之间只有唯一的一条路径。换句话说，所有城市形成了一棵 树 。

# 一棵 子树 是城市的一个子集，且子集中任意城市之间可以通过子集中的其他城市和边到达。两个子树被认为不一样的条件是至少有一个城市在其中一棵子树中存在，
# 但在另一棵子树中不存在。

# 对于 d 从 1 到 n-1 ，请你找到城市间 最大距离 恰好为 d 的所有子树数目。

# 请你返回一个大小为 n-1 的数组，其中第 d 个元素（下标从 1 开始）是城市间 最大距离 恰好等于 d 的子树数目。

# 请注意，两个城市间距离定义为它们之间需要经过的边的数目。


# 示例 1：
# 输入：n = 4, edges = [[1, 2], [2, 3], [2, 4]]
# 输出：[3, 4, 0]
# 解释：
# 子树 {1, 2}, {2, 3} 和 {2, 4} 最大距离都是 1 。
# 子树 {1, 2, 3}, {1, 2, 4}, {2, 3, 4} 和 {1, 2, 3, 4} 最大距离都为 2 。
# 不存在城市间最大距离为 3 的子树。

# 示例 2：
# 输入：n = 2, edges = [[1, 2]]
# 输出：[1]

# 示例 3：
# 输入：n = 3, edges = [[1, 2], [2, 3]]
# 输出：[2, 1]


# 提示：
# 2 <= n <= 15
# edges.length == n-1
# edges[i].length == 2
# 1 <= ui, vi <= n
# 题目保证(ui, vi) 所表示的边互不相同。

# Hard
# 复习

from math import inf
from typing import List
# @lc code=start


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # 计算邻接表和距离
        adj = [[] for _ in range(n)]
        dist = [[inf] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for u, v in edges:
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)
            dist[u][v] = dist[v][u] = 1

        for i in range(n):
            for j in range(n):
                for k in range(j+1, n):
                    if dist[j][i] != inf and dist[i][k] != inf:
                        dist[j][k] = dist[k][j] = min(
                            dist[j][k], dist[j][i]+dist[i][k])

        def dfs(u, parent, x, y):
            if dist[u][x] > dist[x][y] or dist[u][y] > dist[x][y]:
                return 1

            if (dist[u][y] == dist[x][y] and u < x) or (dist[u][x] == dist[x][y] and u < y):
                return 1

            ret = 1
            for v in adj[u]:
                if v != parent:
                    ret *= dfs(v, u, x, y)

            if dist[u][x] + dist[u][y] > dist[x][y]:
                ret += 1

            return ret

        res = [0] * (n - 1)
        for i in range(n-1):
            for j in range(i+1, n):
                res[dist[i][j]-1] += dfs(i, -1, i, j)

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubgraphsForEachDiameter(
        4, [[1, 2], [2, 3], [2, 4]]))  # [3,4,0]
    print(solution.countSubgraphsForEachDiameter(2, [[1, 2]]))  # [1]
    print(solution.countSubgraphsForEachDiameter(3, [[1, 2], [2, 3]]))  # [2,1]
