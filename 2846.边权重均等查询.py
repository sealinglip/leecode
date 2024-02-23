#
# @lc app=leetcode.cn id=2846 lang=python3
#
# [2846] 边权重均等查询
#
# 现有一棵由 n 个节点组成的无向树，节点按从 0 到 n - 1 编号。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ui, vi, wi] 表示树中存在一条位于节点 ui 和节点 vi 之间、权重为 wi 的边。

# 另给你一个长度为 m 的二维整数数组 queries ，其中 queries[i] = [ai, bi] 。对于每条查询，请你找出使从 ai 到 bi 路径上每条边的权重相等所需的 最小操作次数 。在一次操作中，你可以选择树上的任意一条边，并将其权重更改为任意值。

# 注意：
# 查询之间 相互独立 的，这意味着每条新的查询时，树都会回到 初始状态 。
# 从 ai 到 bi的路径是一个由 不同 节点组成的序列，从节点 ai 开始，到节点 bi 结束，且序列中相邻的两个节点在树中共享一条边。
# 返回一个长度为 m 的数组 answer ，其中 answer[i] 是第 i 条查询的答案。

 
# 示例 1：
# 输入：n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]]
# 输出：[0,0,1,3]
# 解释：第 1 条查询，从节点 0 到节点 3 的路径中的所有边的权重都是 1 。因此，答案为 0 。
# 第 2 条查询，从节点 3 到节点 6 的路径中的所有边的权重都是 2 。因此，答案为 0 。
# 第 3 条查询，将边 [2,3] 的权重变更为 2 。在这次操作之后，从节点 2 到节点 6 的路径中的所有边的权重都是 2 。因此，答案为 1 。
# 第 4 条查询，将边 [0,1]、[1,2]、[2,3] 的权重变更为 2 。在这次操作之后，从节点 0 到节点 6 的路径中的所有边的权重都是 2 。因此，答案为 3 。
# 对于每条查询 queries[i] ，可以证明 answer[i] 是使从 ai 到 bi 的路径中的所有边的权重相等的最小操作次数。

# 示例 2：
# 输入：n = 8, edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], queries = [[4,6],[0,4],[6,5],[7,4]]
# 输出：[1,2,2,3]
# 解释：第 1 条查询，将边 [1,3] 的权重变更为 6 。在这次操作之后，从节点 4 到节点 6 的路径中的所有边的权重都是 6 。因此，答案为 1 。
# 第 2 条查询，将边 [0,3]、[3,1] 的权重变更为 6 。在这次操作之后，从节点 0 到节点 4 的路径中的所有边的权重都是 6 。因此，答案为 2 。
# 第 3 条查询，将边 [1,3]、[5,2] 的权重变更为 6 。在这次操作之后，从节点 6 到节点 5 的路径中的所有边的权重都是 6 。因此，答案为 2 。
# 第 4 条查询，将边 [0,7]、[0,3]、[1,3] 的权重变更为 6 。在这次操作之后，从节点 7 到节点 4 的路径中的所有边的权重都是 6 。因此，答案为 3 。
# 对于每条查询 queries[i] ，可以证明 answer[i] 是使从 ai 到 bi 的路径中的所有边的权重相等的最小操作次数。 
 

# 提示：
# 1 <= n <= 10^4
# edges.length == n - 1
# edges[i].length == 3
# 0 <= ui, vi < n
# 1 <= wi <= 26
# 生成的输入满足 edges 表示一棵有效的树
# 1 <= queries.length == m <= 2 * 10^4
# queries[i].length == 2
# 0 <= ai, bi < n

# Hard
# 复习

from collections import deque
from typing import List
# @lc code=start
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        m = n.bit_length()
        g = [[] for _ in range(n)]
        f = [[0] * m for _ in range(n)]
        p = [0] * n
        cnt = [None] * n
        depth = [0] * n
        for u, v, w in edges:
            g[u].append((v, w - 1))
            g[v].append((u, w - 1))
        cnt[0] = [0] * 26
        q = deque([0])
        while q:
            i = q.popleft()
            f[i][0] = p[i]
            for j in range(1, m):
                f[i][j] = f[f[i][j - 1]][j - 1]
            for j, w in g[i]:
                if j != p[i]:
                    p[j] = i
                    cnt[j] = cnt[i][:]
                    cnt[j][w] += 1
                    depth[j] = depth[i] + 1
                    q.append(j)
        res = []
        for u, v in queries:
            x, y = u, v
            if depth[x] < depth[y]:
                x, y = y, x
            for j in reversed(range(m)):
                if depth[x] - depth[y] >= (1 << j):
                    x = f[x][j]
            for j in reversed(range(m)):
                if f[x][j] != f[y][j]:
                    x, y = f[x][j], f[y][j]
            if x != y:
                x = p[x]
            mx = max(cnt[u][j] + cnt[v][j] - 2 * cnt[x][j] for j in range(26))
            res.append(depth[u] + depth[v] - 2 * depth[x] - mx)
            
        return res
    
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperationsQueries(7, [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], [[0,3],[3,6],[2,6],[0,6]])) # [0,0,1,3]
    print(solution.minOperationsQueries(8, [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], [[4,6],[0,4],[6,5],[7,4]])) # [1,2,2,3]