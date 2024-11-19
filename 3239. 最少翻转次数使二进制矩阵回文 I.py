# 给你一个 m x n 的二进制矩阵 grid 。
# 如果矩阵中一行或者一列从前往后与从后往前读是一样的，那么我们称这一行或者这一列是 回文 的。
# 你可以将 grid 中任意格子的值 翻转 ，也就是将格子里的值从 0 变成 1 ，或者从 1 变成 0 。
# 请你返回 最少 翻转次数，使得矩阵 要么 所有行是 回文的 ，要么所有列是 回文的 。


# 示例 1：
# 输入：grid = [[1,0,0],[0,0,0],[0,0,1]]
# 输出：2
# 解释：
# 将高亮的格子翻转，得到所有行都是回文的。

# 示例 2：
# 输入：grid = [[0,1],[0,1],[0,0]]
# 输出：1
# 解释：
# 将高亮的格子翻转，得到所有列都是回文的。

# 示例 3：
# 输入：grid = [[1],[0]]
# 输出：0
# 解释：
# 所有行已经是回文的。

# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m * n <= 2 * 10^5
# 0 <= grid[i][j] <= 1

from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        diff_row = 0
        for i in range(m):  # 统计行差异
            for j in range(n // 2):
                if grid[i][j] != grid[i][n - 1 - j]:
                    diff_row += 1

        diff_col = 0
        for j in range(n):  # 统计列差异
            for i in range(m // 2):
                if grid[i][j] != grid[m - 1 - i][j]:
                    diff_col += 1

        return min(diff_row, diff_col)

if __name__ == "__main__":
    solution = Solution()
    print(solution.minFlips([[1,0,0],[0,0,0],[0,0,1]])) # 2
    print(solution.minFlips([[0,1],[0,1],[0,0]])) # 1
    print(solution.minFlips([[1],[0]])) # 0
    