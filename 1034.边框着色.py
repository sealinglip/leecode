#
# @lc app=leetcode.cn id=1034 lang=python3
#
# [1034] 边框着色
#
# 给你一个大小为 m x n 的整数矩阵 grid ，表示一个网格。另给你三个整数 row、col 和 color 。网格中的每个值表示该位置处的网格块的颜色。

# 两个网格块属于同一 连通分量 需满足下述全部条件：

# 两个网格块颜色相同
# 在上、下、左、右任意一个方向上相邻
# 连通分量的边界 是指连通分量中满足下述条件之一的所有网格块：

# 在上、下、左、右四个方向上与不属于同一连通分量的网格块相邻
# 在网格的边界上（第一行/列或最后一行/列）
# 请你使用指定颜色 color 为所有包含网格块 grid[row][col] 的 连通分量的边界 进行着色，并返回最终的网格 grid 。


# 示例 1：
# 输入：grid = [[1, 1], [1, 2]], row = 0, col = 0, color = 3
# 输出：[[3, 3], [3, 2]]

# 示例 2：
# 输入：grid = [[1, 2, 2], [2, 3, 2]], row = 0, col = 1, color = 3
# 输出：[[1, 3, 3], [2, 3, 3]]

# 示例 3：
# 输入：grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]], row = 1, col = 1, color = 2
# 输出：[[2, 2, 2], [2, 1, 2], [2, 2, 2]]


# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j], color <= 1000
# 0 <= row < m
# 0 <= col < n


from typing import List
# @lc code=start


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = {}

        def dfs(x: int, y: int, c: int) -> bool:
            if grid[x][y] == c:
                p = (x, y)
                if p not in visited:
                    visited[p] = False
                    # 环顾四周
                    edge = False
                    for dx, dy in DIR:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < M and 0 <= ny < N:
                            if not dfs(nx, ny, c):
                                edge = True
                        else:
                            edge = True  # 在边界上
                    visited[p] = edge
                return True
            return False

        dfs(row, col, grid[row][col])

        for (x, y), f in visited.items():
            if f:
                grid[x][y] = color
        return grid
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.colorBorder([[1, 1], [1, 2]], 0, 0, 3))  # [[3, 3], [3, 2]]
    print(solution.colorBorder([[1, 2, 2], [2, 3, 2]],
                               0, 1, 3))  # [[1, 3, 3], [2, 3, 3]]
    print(solution.colorBorder([[1, 1, 1], [1, 1, 1], [
          1, 1, 1]], 1, 1, 2))  # [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
