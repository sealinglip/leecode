#
# @lc app=leetcode.cn id=1489 lang=python3
#
# [1489] 找到最小生成树里的关键边和伪关键边
#
# 给你一个 n 个点的带权无向连通图，节点编号为 0 到 n-1 ，同时还有一个数组 edges ，其中 edges[i] = [fromi, toi, weighti] 表示在 fromi 和 toi 节点之间有一条带权无向边。最小生成树(MST) 是给定图中边的一个子集，它连接了所有节点且没有环，而且这些边的权值和最小。
# 请你找到给定图中最小生成树的所有关键边和伪关键边。如果从图中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。伪关键边则是可能会出现在某些最小生成树中但不会出现在所有最小生成树中的边。
# 请注意，你可以分别以任意顺序返回关键边的下标和伪关键边的下标。

# 示例 1：
# 输入：n = 5, edges = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]
# 输出：[[0, 1], [2, 3, 4, 5]]
# 解释：上图描述了给定图。
# 下图是所有的最小生成树。
# 注意到第 0 条边和第 1 条边出现在了所有最小生成树中，所以它们是关键边，我们将这两个下标作为输出的第一个列表。
# 边 2，3，4 和 5 是所有 MST 的剩余边，所以它们是伪关键边。我们将它们作为输出的第二个列表。

# 示例 2 ：
# 输入：n = 4, edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]
# 输出：[[], [0, 1, 2, 3]]
# 解释：可以观察到 4 条边都有相同的权值，任选它们中的 3 条可以形成一棵 MST 。所以 4 条边都是伪关键边。

# 提示：
# 2 <= n <= 100
# 1 <= edges.length <= min(200, n * (n - 1) / 2)
# edges[i].length == 3
# 0 <= fromi < toi < n
# 1 <= weighti <= 1000
# 所有(fromi, toi) 数对都是互不相同的。

# Hard

from typing import List
# @lc code=start


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parent = list(range(n))

        def find(idx: int) -> int:
            if idx != parent[idx]:
                parent[idx] = find(parent[idx])
            return parent[idx]

        def union(idx1: int, idx2: int):
            parent[idx2] = idx1

        sorted_edges = [[i] + e for i, e in enumerate(edges)]
        # 根据权重对边排序
        sorted_edges.sort(key=lambda x: x[-1])

        # 计算最小生成🌲的权值和
        total = 0
        for _, x, y, w in sorted_edges:
            rx, ry = find(x), find(y)
            if rx != ry:
                union(rx, ry)
                total += w

        # 进行最小生成🌲的构造
        key_edge = []  # 关键边
        not_key_edge = []  # 非关键边
        for i, edge in enumerate(sorted_edges):
            _, cx, cy, cw = edge
            # 去掉当前边，形成新的边列表
            tmp_edges = sorted_edges[:i] + sorted_edges[i+1:]

            # 1. 先连接当前边，得到连通边的权值和 total1
            total1 = cw
            parent = list(range(n))
            union(cx, cy)
            for i, (_, x, y, w) in enumerate(tmp_edges):
                rx, ry = find(x), find(y)
                if rx != ry:
                    union(rx, ry)
                    total1 += w

            # 若 total和total1相等，表示该边为可能的关键边
            if total != total1:
                continue

            # 2. 去掉当前边，得到的连通边权值和 total2
            total2 = 0
            parent = list(range(n))
            for i, (_, x, y, w) in enumerate(tmp_edges):
                rx, ry = find(x), find(y)
                if rx != ry:
                    union(rx, ry)
                    total2 += w

            # 若 total1不等于total2，则代表该边为 关键边，否则为伪关键边
            if total1 != total2:
                key_edge.append(edge[0])
            else:
                not_key_edge.append(edge[0])

        return [key_edge, not_key_edge]


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findCriticalAndPseudoCriticalEdges(5, [[0, 1, 1], [
          1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]))
    print(solution.findCriticalAndPseudoCriticalEdges(
        4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]))
