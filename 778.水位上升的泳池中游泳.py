#
# @lc app=leetcode.cn id=778 lang=python3
#
# [778] 水位上升的泳池中游泳
#
# 在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置(i, j) 的平台高度。
# 现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。
# 你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。
# 假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。
# 你从坐标方格的左上平台(0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台(N-1, N-1)？

# 示例 1:
# 输入: [[0, 2], [1, 3]]
# 输出: 3
# 解释:
# 时间为0时，你位于坐标方格的位置为(0, 0)。
# 此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。

# 等时间到达 3 时，你才可以游向平台(1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置

# 示例2:
# 输入: [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [
#     12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
# 输出: 16
# 解释:
#  0  1  2  3  4
# 24 23 22 21  5
# 12 13 14 15 16
# 11 17 18 19 20
# 10  9  8  7  6

# 最终的路线用加粗进行了标记。
# 我们必须等到时间为 16，此时才能保证平台(0, 0) 和(4, 4) 是连通的

# 提示:
# 2 <= N <= 50.
# grid[i][j] 是[0, ..., N*N - 1] 的排列。

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
    def swimInWater(self, grid: List[List[int]]) -> int:
        # 将每一个格子看成图中的一个节点
        # 将两个相邻（左右相邻或者上下相邻）的两个格子对应的节点之间连接一条无向边，边的权重为这两个格子的高度最大值
        # 需要找到一条从左上角到右下角的最短路径（代表了最短耗时），其中一条路径的长度定义为其经过的所有边权的最大值

        # 将这 N*N 个节点放入并查集中，实时维护它们的连通性
        # 要找到从左上角到右下角的最短路径，可以将图中的所有边按照权值从小到大进行排序，并依次加入并查集中
        # 当加入一条权值为 x 的边之后，如果左上角和右下角从非连通状态变为连通状态，那么 x 即为答案
        N = len(grid)

        edges = []
        for i in range(N):
            for j in range(N):
                idx = i * N + j
                if i > 0:
                    edges.append(
                        (idx - N, idx, max(grid[i][j], grid[i - 1][j])))
                if j > 0:
                    edges.append(
                        (idx - 1, idx, max(grid[i][j], grid[i][j - 1])))

        edges.sort(key=lambda e: e[2])

        uf = UnionFind(N * N)
        res = 0
        sIdx, eIdx = 0, N * N - 1
        for e in edges:
            uf.union(e[0], e[1])
            if uf.isConnected(sIdx, eIdx):
                res = e[2]
                break

        return res

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.swimInWater([[0, 2], [1, 3]]))
    print(solution.swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [
          12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))
