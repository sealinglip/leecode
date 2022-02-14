#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#
# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。

# 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。

# 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。


# 示例 1：
# 输入：grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
# 输出：3
# 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。

# 示例 2：
# 输入：grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
# 输出：0
# 解释：所有 1 都在边界上或可以到达边界。


# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] 的值为 0 或 1


from typing import List
# @lc code=start


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        DIR = ((1, 0), (-1, 0), (0, 1), (0, -1))
        # 从边上遍历，找为1的单元格，相邻的都赋值成0，最后找不为零的单元格数量
        m, n = len(grid), len(grid[0])

        def dfs(x: int, y: int):
            if grid[x][y] == 1:
                grid[x][y] = 0
                for dx, dy in DIR:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        dfs(nx, ny)

        for c in range(n):
            dfs(0, c)
            dfs(m-1, c)

        for r in range(1, m-1):
            dfs(r, 0)
            dfs(r, n-1)

        return sum([sum(row, 0) for row in grid], 0)
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.numEnclaves(
        [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))  # 3
    print(solution.numEnclaves(
        [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))  # 0
