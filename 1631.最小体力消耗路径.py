#
# @lc app=leetcode.cn id=1631 lang=python3
#
# [1631] 最小体力消耗路径
#

from typing import List
# @lc code=start
# 并查集


class UnionFind:
    def __init__(self, n: int):
        self.group = list(range(n))

    def findGroup(self, x: int) -> int:
        if self.group[x] == x:
            return x
        self.group[x] = self.findGroup(self.group[x])
        return self.group[x]

    def union(self, x: int, y: int):
        x, y = self.findGroup(x), self.findGroup(y)
        if x != y:
            self.group[x] = y

    def isConnected(self, x: int, y: int) -> bool:
        return self.findGroup(x) == self.findGroup(y)


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # 将地图中的每一个格子看成图中的一个节点
        # 将两个相邻（左右相邻或者上下相邻）的两个格子对应的节点之间连接一条无向边，边的权重为这两个格子的高度差的绝对值
        # 需要找到一条从左上角到右下角的最短路径，其中一条路径的长度定义为其经过的所有边权的最大值

        # 将这 mn 个节点放入并查集中，实时维护它们的连通性
        # 要找到从左上角到右下角的最短路径，可以将图中的所有边按照权值从小到大进行排序，并依次加入并查集中
        # 当加入一条权值为 x 的边之后，如果左上角和右下角从非连通状态变为连通状态，那么 x 即为答案

        M, N = len(heights), len(heights[0])

        edges = []
        for i in range(M):
            for j in range(N):
                idx = i * N + j  # 把二维坐标转为一维
                if i > 0:
                    edges.append(
                        (idx - N, idx, abs(heights[i][j] - heights[i - 1][j])))
                if j > 0:
                    edges.append(
                        (idx - 1, idx, abs(heights[i][j] - heights[i][j - 1])))

        edges.sort(key=lambda e: e[2])

        uf = UnionFind(N * M)
        sIdx, eIdx = 0, N * M - 1
        for e in edges:
            uf.union(e[0], e[1])
            if uf.isConnected(sIdx, eIdx):
                return e[2]

        return 0

        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumEffortPath([[3]]))
    print(solution.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
    print(solution.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
    print(solution.minimumEffortPath([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [
          1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))
