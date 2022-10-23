#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#
# 给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。

# 给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和  bi的人归入同一组。当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。


# 示例 1：
# 输入：n = 4, dislikes = [[1, 2], [1, 3], [2, 4]]
# 输出：true
# 解释：group1[1, 4], group2[2, 3]

# 示例 2：
# 输入：n = 3, dislikes = [[1, 2], [1, 3], [2, 3]]
# 输出：false

# 示例 3：
# 输入：n = 5, dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
# 输出：false


# 提示：
# 1 <= n <= 2000
# 0 <= dislikes.length <= 10^4
# dislikes[i].length == 2
# 1 <= dislikes[i][j] <= n
# ai < bi
# dislikes 中每一组都 不同

# 并查集

from typing import List
# @lc code=start


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [1] * n  # 决定合并时的方向：小集合合并到大集合

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.rank[fx] += self.rank[fy]
        self.parent[fy] = fx

    def isConnected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for x, y in dislikes:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        uf = UnionFind(n)
        for x, dis in enumerate(graph):
            for y in dis:
                uf.union(dis[0], y)
                if uf.isConnected(x, y):
                    return False

        return True

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]))  # True
    print(solution.possibleBipartition(3, [[1, 2], [1, 3], [2, 3]]))  # False
    print(solution.possibleBipartition(
        5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))  # False
