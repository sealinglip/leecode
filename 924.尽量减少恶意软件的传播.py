#
# @lc app=leetcode.cn id=924 lang=python3
#
# [924] 尽量减少恶意软件的传播
#
# 给出了一个由 n 个节点组成的网络，用 n × n 个邻接矩阵图 graph 表示。在节点网络中，当 graph[i][j] = 1 时，表示节点 i 能够直接连接到另一个节点 j。 

# 一些节点 initial 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。这种恶意软件的传播将继续，直到没有更多的节点可以被这种方式感染。

# 假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。

# 如果从 initial 中移除某一节点能够最小化 M(initial)， 返回该节点。如果有多个节点满足条件，就返回索引最小的节点。

# 请注意，如果某个节点已从受感染节点的列表 initial 中删除，它以后仍有可能因恶意软件传播而受到感染。


# 示例 1：
# 输入：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
# 输出：0

# 示例 2：
# 输入：graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]
# 输出：0

# 示例 3：
# 输入：graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2]
# 输出：1
 

# 提示：
# n == graph.length
# n == graph[i].length
# 2 <= n <= 300
# graph[i][j] == 0 或 1.
# graph[i][j] == graph[j][i]
# graph[i][i] == 1
# 1 <= initial.length <= n
# 0 <= initial[i] <= n - 1
# initial 中所有整数均不重复

# Hard
# 复习

from typing import List, Tuple
# @lc code=start
class UnionFind:
    def __init__(self, n: int, initial: List[int]) -> None:
        self.group = list(range(n))
        self.groupSize = [1] * n
        self.infected = [0] * n
        for i in initial:
            self.infected[i] = 1
        self.n = n
        self.groupCnt = n

    def find(self, x: int) -> int:
        if self.group[x] == x:
            return x
        self.group[x] = self.find(self.group[x])
        return self.group[x]
    
    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y: # 已经是一组
            return False
        if self.groupSize[x] < self.groupSize[y]:
            x, y = y, x
        self.group[y] = x # 小集合合并到大集合
        self.groupSize[x] += self.groupSize[y]
        self.groupSize[y] = 0
        self.infected[x] += self.infected[y]
        self.infected[y] = 0
        self.groupCnt -= 1
        return True
    
    def isConnected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def getGroup(self, x: int) -> Tuple[int]:
        x = self.group[x]
        return (x, self.groupSize[x], self.infected[x])
        

class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        # 并查集求连通分量及每个连通分量感染节点个数，如果某个连通分量初始感染节点个数大于1，不用处理，搞也没用，
        # 如果某个连通分量有且只有一个初始感染节点，那么可以处理一下
        uf = UnionFind(n, initial)
        for i in range(n):
            for j in range(i + 1, n):
                if graph[i][j] == 1:
                    uf.union(i, j)
        
        
        initial.sort()
        res = (0, initial[0])
        for i in initial:
            x, gs, gi = uf.getGroup(i)
            if gi == 1:
                if gs > res[0]:
                    res = (gs, i)
        return res[1]

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minMalwareSpread([[1,1,0],[1,1,0],[0,0,1]], [0,1])) # 0
    print(solution.minMalwareSpread([[1,0,0],[0,1,0],[0,0,1]], [0,2])) # 0
    print(solution.minMalwareSpread([[1,1,1],[1,1,1],[1,1,1]], [1,2])) # 1