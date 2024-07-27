#
# @lc app=leetcode.cn id=1463 lang=python3
#
# [1463] 摘樱桃 II
#
# 给你一个 rows x cols 的矩阵 grid 来表示一块樱桃地。 grid 中每个格子的数字表示你能获得的樱桃数目。

# 你有两个机器人帮你收集樱桃，机器人 1 从左上角格子 (0,0) 出发，机器人 2 从右上角格子 (0, cols-1) 出发。

# 请你按照如下规则，返回两个机器人能收集的最多樱桃数目：

# 从格子 (i,j) 出发，机器人可以移动到格子 (i+1, j-1)，(i+1, j) 或者 (i+1, j+1) 。
# 当一个机器人经过某个格子时，它会把该格子内所有的樱桃都摘走，然后这个位置会变成空格子，即没有樱桃的格子。
# 当两个机器人同时到达同一个格子时，它们中只有一个可以摘到樱桃。
# 两个机器人在任意时刻都不能移动到 grid 外面。
# 两个机器人最后都要到达 grid 最底下一行。
 

# 示例 1：
# 输入：grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# 输出：24
# 解释：机器人 1 和机器人 2 的路径在上图中分别用绿色和蓝色表示。
# 机器人 1 摘的樱桃数目为 (3 + 2 + 5 + 2) = 12 。
# 机器人 2 摘的樱桃数目为 (1 + 5 + 5 + 1) = 12 。
# 樱桃总数为： 12 + 12 = 24 。

# 示例 2：
# 输入：grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
# 输出：28
# 解释：机器人 1 和机器人 2 的路径在上图中分别用绿色和蓝色表示。
# 机器人 1 摘的樱桃数目为 (1 + 9 + 5 + 2) = 17 。
# 机器人 2 摘的樱桃数目为 (1 + 3 + 4 + 3) = 11 。
# 樱桃总数为： 17 + 11 = 28 。

# 示例 3：
# 输入：grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
# 输出：22

# 示例 4：
# 输入：grid = [[1,1],[1,1]]
# 输出：4
 

# 提示：
# rows == grid.length
# cols == grid[i].length
# 2 <= rows, cols <= 70
# 0 <= grid[i][j] <= 100 

# Hard

from math import inf
from typing import List
# @lc code=start
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 动规
        # 记dp(k, x1, x2) 为两个机器人分别处于第k行，x1列和x2列的时候，最大收益
        # 初始 dp(0, 0, n-1) = grid[0][0] + grid[0][n-1], 其他dp(0, *, *) = -∞
        # 状态转移方程：
        # dp(k, x1, x2) = max(dp(k-1, [前一行位置的有效组合])) + grid[k][x1] + grid[k][x2] if x1 != x2 else 0
        dp = [[-inf] * n for _ in range(n)]
        dp[0][n-1] = grid[0][0] + grid[0][n-1]
        for k in range(1, m):
            newDp = [[-inf] * n for _ in range(n)]
            for x1 in range(k+1): # x1的范围
                for x2 in range(max(x1, n-k-1), n):
                    best = 0
                    for dx1, dx2 in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        nx1, nx2 = x1 + dx1, x2 + dx2
                        if 0 <= nx1 < n and 0 <= nx2 < n:
                            best = max(best, dp[nx1][nx2])
                    best += grid[k][x1] + grid[k][x2] if x1 != x2 else 0
                    newDp[x1][x2] = best

            dp = newDp

        return max(max(row) for row in dp)
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]])) # 24
    print(solution.cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]])) # 28
    print(solution.cherryPickup([[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]])) # 22
    print(solution.cherryPickup([[1,1],[1,1]])) # 4