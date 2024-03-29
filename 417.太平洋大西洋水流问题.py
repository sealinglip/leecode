#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#
# 有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。

# 这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标(r, c) 上单元格 高于海平面的高度 。

# 岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。

# 返回 网格坐标 result 的 2D列表 ，其中 result[i] = [ri, ci] 表示雨水可以从单元格(ri, ci) 流向 太平洋和大西洋 。


# 示例 1：
# 输入: heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
#     2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
# 输出: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

# 示例 2：
# 输入: heights = [[2, 1], [1, 2]]
# 输出: [[0, 0], [0, 1], [1, 0], [1, 1]]


# 提示：
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 10^5

from typing import List, Set, Tuple
# @lc code=start
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def bfs(start: List[Tuple[int]]) -> Set[Tuple[int]]:
            visited = set(start)
            q = deque(start)
            while q:
                x, y = q.popleft()
                # 从pos往四周找不低于自己的区域
                for newp in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
                    if 0 <= newp[0] < m and 0 <= newp[1] < n and heights[newp[0]][newp[1]] >= heights[x][y] and newp not in visited:
                        visited.add(newp)
                        q.append(newp)
            return visited

        pacific = [(0, x) for x in range(n)] + [(y, 0) for y in range(1, m)]
        atlantic = [(m-1, x)
                    for x in range(n)] + [(y, n-1) for y in range(m-1)]
        return list(map(list, bfs(pacific) & bfs(atlantic)))

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
        2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))  # [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    # [[0, 0], [0, 1], [1, 0], [1, 1]]
    print(solution.pacificAtlantic([[2, 1], [1, 2]]))
