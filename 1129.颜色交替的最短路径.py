#
# @lc app=leetcode.cn id=1129 lang=python3
#
# [1129] 颜色交替的最短路径
#
# 在一个有向图中，节点分别标记为 0, 1, ..., n-1。图中每条边为红色或者蓝色，且存在自环或平行边。

# red_edges 中的每一个[i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，blue_edges 中的每一个[i, j] 对表示从节点 i 到节点 j 的蓝色有向边。

# 返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 answer[x] = -1。


# 示例 1：
# 输入：n = 3, red_edges = [[0, 1], [1, 2]], blue_edges = []
# 输出：[0, 1, -1]

# 示例 2：
# 输入：n = 3, red_edges = [[0, 1]], blue_edges = [[2, 1]]
# 输出：[0, 1, -1]

# 示例 3：
# 输入：n = 3, red_edges = [[1, 0]], blue_edges = [[2, 1]]
# 输出：[0, -1, -1]

# 示例 4：
# 输入：n = 3, red_edges = [[0, 1]], blue_edges = [[1, 2]]
# 输出：[0, 1, 2]

# 示例 5：
# 输入：n = 3, red_edges = [[0, 1], [0, 2]], blue_edges = [[1, 0]]
# 输出：[0, 1, 1]

# 提示：
# 1 <= n <= 100
# red_edges.length <= 400
# blue_edges.length <= 400
# red_edges[i].length == blue_edges[i].length == 2
# 0 <= red_edges[i][j], blue_edges[i][j] < n

from collections import defaultdict
from typing import List
# @lc code=start


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [-1] * n
        res[0] = 0

        # prepare
        def buildPath(edges: List[List[int]], pathDict) -> None:
            for s, e in edges:
                pathDict[s].add(e)

        redPath = defaultdict(set)
        bluePath = defaultdict(set)
        buildPath(redEdges, redPath)
        buildPath(blueEdges, bluePath)
        pathDicts = [redPath, bluePath]

        # bfs
        p = [(0, 0), (0, 1)]  # 分别代表从0开始，下一步可以是红边或蓝边
        visited = set(p)
        step = 0
        while p:
            step += 1
            newp = []
            for src, color in p:
                for d in [(x, 1-color) for x in pathDicts[color][src]]:
                    if d not in visited:
                        newp.append(d)
                        visited.add(d)
                        if res[d[0]] == -1:
                            res[d[0]] = step

            p = newp

        return res
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.shortestAlternatingPaths(
        5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[1, 2], [2, 3], [3, 1]]))  # [0,1,2,3,7]
    print(solution.shortestAlternatingPaths(
        3, [[0, 1], [1, 2]], []))  # [0,1,-1]
    print(solution.shortestAlternatingPaths(3, [[0, 1]], [[2, 1]]))  # [0,1,-1]
    print(solution.shortestAlternatingPaths(
        3, [[1, 0]], [[2, 1]]))  # [0,-1,-1]
    print(solution.shortestAlternatingPaths(3, [[0, 1]], [[1, 2]]))  # [0,1,2]
    print(solution.shortestAlternatingPaths(
        3, [[0, 1], [0, 2]], [[1, 0]]))  # [0,1,1]
