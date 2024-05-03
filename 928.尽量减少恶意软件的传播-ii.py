#
# @lc app=leetcode.cn id=928 lang=python3
#
# [928] 尽量减少恶意软件的传播 II
#
# 给定一个由 n 个节点组成的网络，用 n x n 个邻接矩阵 graph 表示。在节点网络中，只有当 graph[i][j] = 1 时，节点 i 能够直接连接到另一个节点 j。

# 一些节点 initial 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。这种恶意软件的传播将继续，直到没有更多的节点可以被这种方式感染。

# 假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。

# 我们可以从 initial 中删除一个节点，并完全移除该节点以及从该节点到任何其他节点的任何连接。

# 请返回移除后能够使 M(initial) 最小化的节点。如果有多个节点满足条件，返回索引 最小的节点 。


# 示例 1：
# 输入：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
# 输出：0

# 示例 2：
# 输入：graph = [[1,1,0],[1,1,1],[0,1,1]], initial = [0,1]
# 输出：1

# 示例 3：
# 输入：graph = [[1,1,0,0],[1,1,1,0],[0,1,1,1],[0,0,1,1]], initial = [0,1]
# 输出：1
 

# 提示：
# n == graph.length
# n == graph[i].length
# 2 <= n <= 300
# graph[i][j] 是 0 或 1.
# graph[i][j] == graph[j][i]
# graph[i][i] == 1
# 1 <= initial.length < n
# 0 <= initial[i] <= n - 1
#  initial 中每个整数都不同

# Hard

from typing import List
# @lc code=start
class Solution:
    def find(self, uf: List[int], u: int) -> int:
        if uf[u] == u:
            return u
        uf[u] = self.find(uf, uf[u])
        return uf[u]
    
    def merge(self, uf: List[int], u: int, v: int) -> None:
        ru, rv = self.find(uf, u), self.find(uf, v)
        uf[ru] = rv

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        initial = set(initial)
        # 并查集（只针对正常节点构建）
        uf = list(range(n))
        for u in range(n):
            if u in initial:
                continue
            for v in range(n):
                if v in initial:
                    continue
                if graph[u][v] == 1:
                    self.merge(uf, u, v)

        infectedBy = [[] for _ in range(n)]
        for v in initial:
            infectedSet = set()
            for u in range(n):
                if u in initial or graph[u][v] == 0:
                    continue
                infectedSet.add(self.find(uf, u))
            for u in range(n):
                if u in infectedSet:
                    infectedBy[u].append(v)
        
        count = [0] * n
        for u in range(n):
            if len(infectedBy[u]) != 1:
                continue
            v = infectedBy[u][0] # u只能被v感染
            for w in range(n):
                if self.find(uf, w) == self.find(uf, u):
                    count[v] += 1

        res = initial.pop()
        for v in initial:
            if count[v] > count[res] or (count[v] == count[res] and v < res):
                res = v
        return res

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minMalwareSpread([[1,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,1],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,1,0,0,0,0,0,1]], [2,1,9])) # 9
    print(solution.minMalwareSpread([[1,1,0],[1,1,0],[0,0,1]], [0,1])) # 0
    print(solution.minMalwareSpread([[1,1,0],[1,1,1],[0,1,1]], [0,1])) # 1
    print(solution.minMalwareSpread([[1,1,0,0],[1,1,1,0],[0,1,1,1],[0,0,1,1]], [0,1])) # 1