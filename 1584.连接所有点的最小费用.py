#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#
# 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
# 连接点[xi, yi] 和点[xj, yj] 的费用为它们之间的 曼哈顿距离 ：| xi - xj | + | yi - yj | ，其中 | val | 表示 val 的绝对值。
# 请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。

# 示例 1：
# 输入：points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
# 输出：20
# 解释：
# 我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
# 注意到任意两个点之间只有唯一一条路径互相到达。

# 示例 2：
# 输入：points = [[3, 12], [-2, 5], [-4, 1]]
# 输出：18

# 示例 3：
# 输入：points = [[0, 0], [1, 1], [1, 0], [-1, 1]]
# 输出：4

# 示例 4：
# 输入：points = [[-1000000, -1000000], [1000000, 1000000]]
# 输出：4000000

# 示例 5：
# 输入：points = [[0, 0]]
# 输出：0


# 提示：
# 1 <= points.length <= 1000
# -106 <= xi, yi <= 10^6
# 所有点(xi, yi) 两两不同。

from typing import List
# @lc code=start


class UnionFind:
    def __init__(self):
        self.group = {}

    def _get_(self, x):
        return self.group.get(x, x)

    def find(self, x):
        while self._get_(x) != x:
            self.group[x] = self._get_(self._get_(x))
            x = self._get_(x)
        return x

    def merge(self, x, y):
        self.group[self.find(x)] = self.find(y)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        if N <= 1:
            return 0

        # 计算任意两点之间的费用
        costs = []
        for i in range(N - 1):
            for j in range(1, N):
                cost = abs(points[j][0] - points[i][0]) + \
                    abs(points[j][1] - points[i][1])
                costs.append((cost, i, j))
        costs.sort(key=lambda c: c[0])  # 按费用从低到高排列

        res = 0
        uf = UnionFind()
        for cost, i, j in costs:
            if uf.find(i) != uf.find(j):
                uf.merge(i, j)  # 连接i，j
                res += cost
        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minCostConnectPoints(
        [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
    print(solution.minCostConnectPoints(
        [[3, 12], [-2, 5], [-4, 1]]))
    print(solution.minCostConnectPoints(
        [[0, 0], [1, 1], [1, 0], [-1, 1]]))
    print(solution.minCostConnectPoints(
        [[-1000000, -1000000], [1000000, 1000000]]))
    print(solution.minCostConnectPoints([[0, 0]]))
