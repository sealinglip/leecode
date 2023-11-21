#
# @lc app=leetcode.cn id=310 lang=python3
#
# [310] 最小高度树
#
# 树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。

# 给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。

# 可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。

# 请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。

# 树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。


# 示例 1：
# 输入：n = 4, edges = [[1, 0], [1, 2], [1, 3]]
# 输出：[1]
# 解释：如图所示，当根是标签为 1 的节点时，树的高度是 1 ，这是唯一的最小高度树。


# 示例 2：
# 输入：n = 6, edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
# 输出：[3, 4]


# 提示：
# 1 <= n <= 2 * 10^4
# edges.length == n - 1
# 0 <= ai, bi < n
# ai != bi
# 所有(ai, bi) 互不相同
# 给定的输入 保证 是一棵树，并且 不会有重复的边

# 复习

from typing import List
# @lc code=start
from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]  # 构建邻接表
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        parents = [0] * n  # 记录在dfs过程中，节点的上级

        def dfs(start: int) -> int:
            '''
            以节点start为起点，找到最远路径对应的节点返回
            如果最远路径有多个，返回最后一条最长路径对应的节点
            '''
            visited = [False] * n
            visited[start] = True
            q = deque([start])
            while q:
                cur = q.popleft()
                for child in g[cur]:
                    if not visited[child]:
                        visited[child] = True
                        parents[child] = cur
                        q.append(child)
            return cur  # 最远的节点

        x = dfs(0)  # x和0最远
        y = dfs(x)  # y和x最远

        # 要求的根节点在x到y的路径上
        path = []
        parents[x] = -1
        while y != -1:
            path.append(y)
            y = parents[y]

        m = len(path)  # 最远节点路径长度
        return [path[m // 2]] if m & 1 else [path[m // 2 - 1], path[m // 2]]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
    print(solution.findMinHeightTrees(
        6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
