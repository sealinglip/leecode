#
# @lc app=leetcode.cn id=1210 lang=python3
#
# [1210] 穿过迷宫的最少移动次数
#
# 你还记得那条风靡全球的贪吃蛇吗？

# 我们在一个 n*n 的网格上构建了新的迷宫地图，蛇的长度为 2，也就是说它会占去两个单元格。蛇会从左上角（(0, 0) 和(0, 1)）开始移动。我们用 0 表示空单元格，用 1 表示障碍物。蛇需要移动到迷宫的右下角（(n-1, n-2) 和(n-1, n-1)）。

# 每次移动，蛇可以这样走：

# 如果没有障碍，则向右移动一个单元格。并仍然保持身体的水平／竖直状态。
# 如果没有障碍，则向下移动一个单元格。并仍然保持身体的水平／竖直状态。
# 如果它处于水平状态并且其下面的两个单元都是空的，就顺时针旋转 90 度。蛇从（(r, c)、(r, c+1)）移动到 （(r, c)、(r+1, c)）。

# 如果它处于竖直状态并且其右面的两个单元都是空的，就逆时针旋转 90 度。蛇从（(r, c)、(r+1, c)）移动到（(r, c)、(r, c+1)）。

# 返回蛇抵达目的地所需的最少移动次数。

# 如果无法到达目的地，请返回 -1。


# 示例 1：
# 输入：grid = [[0, 0, 0, 0, 0, 1],
#            [1, 1, 0, 0, 1, 0],
#            [0, 0, 0, 0, 1, 1],
#            [0, 0, 1, 0, 1, 0],
#            [0, 1, 1, 0, 0, 0],
#            [0, 1, 1, 0, 0, 0]]
# 输出：11
# 解释：
# 一种可能的解决方案是[右, 右, 顺时针旋转, 右, 下, 下, 下, 下, 逆时针旋转, 右, 下]。

# 示例 2：
# 输入：grid = [[0, 0, 1, 1, 1, 1],
#            [0, 0, 0, 0, 1, 1],
#            [1, 1, 0, 0, 0, 1],
#            [1, 1, 1, 0, 0, 1],
#            [1, 1, 1, 0, 0, 1],
#            [1, 1, 1, 0, 0, 0]]
# 输出：9


# 提示：
# 2 <= n <= 100
# 0 <= grid[i][j] <= 1
# 蛇保证从空单元格开始出发。

# Hard
# 复习
# 动规

from math import inf
from typing import List
# @lc code=start


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 记dp(x, y, status) 为 🐍尾从初始态移动到 x, y，状态status（0：水平，1：垂直）所需的最少步数
        # 那么有 dp(0, 0, 0) = 0
        # 状态有效时：
        # dp(x, y, 0) = min(dp(x-1, y, 0), dp(x, y-1, 0), dp(x, y, 1)) + 1
        # dp(x, y, 1) = min(dp(x-1, y, 1), dp(x, y-1, 1), dp(x, y, 0)) + 1
        # 如果状态无效，则dp(x, y, statue) = ∞
        # 最终答案要求dp(n-2, n-1, 0)
        # 又dp只向前依赖，状态可以压缩
        dp = None

        for y in range(n):
            newDp = [[inf, inf] for _ in range(n)]
            if y == 0:
                newDp[0][0] = 0
            for x in range(n):
                # 判断当前状态
                canHor = x < n - 1 and grid[y][x] == 0 and grid[y][x + 1] == 0
                canVer = y < n - 1 and grid[y][x] == 0 and grid[y + 1][x] == 0
                canRotate = canHor and canVer and grid[y + 1][x + 1] == 0

                if x - 1 >= 0 and canHor:
                    newDp[x][0] = min(newDp[x][0], newDp[x-1][0] + 1)
                if y - 1 >= 0 and canHor:
                    newDp[x][0] = min(newDp[x][0], dp[x][0] + 1)
                if x - 1 >= 0 and canVer:
                    newDp[x][1] = min(newDp[x][1], newDp[x-1][1] + 1)
                if y - 1 >= 0 and canVer:
                    newDp[x][1] = min(newDp[x][1], dp[x][1] + 1)
                if canRotate:
                    newDp[x][0] = min(newDp[x][0], newDp[x][1] + 1)
                    newDp[x][1] = min(newDp[x][1], newDp[x][0] + 1)
            dp = newDp

        return dp[n-2][0] if dp[n-2][0] != inf else -1

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumMoves([[0, 0, 0, 0, 1, 1],
                                 [1, 1, 0, 0, 0, 1],
                                 [1, 1, 1, 0, 0, 1],
                                 [1, 1, 1, 0, 1, 1],
                                 [1, 1, 1, 0, 0, 1],
                                 [1, 1, 1, 0, 0, 0]]))  # 11
    print(solution.minimumMoves([[0, 0, 0, 0, 0, 1],
                                 [1, 1, 0, 0, 1, 0],
                                 [0, 0, 0, 0, 1, 1],
                                 [0, 0, 1, 0, 1, 0],
                                 [0, 1, 1, 0, 0, 0],
                                 [0, 1, 1, 0, 0, 0]]))  # 11
    print(solution.minimumMoves([[0, 0, 1, 1, 1, 1],
                                 [0, 0, 0, 0, 1, 1],
                                 [1, 1, 0, 0, 0, 1],
                                 [1, 1, 1, 0, 0, 1],
                                 [1, 1, 1, 0, 0, 1],
                                 [1, 1, 1, 0, 0, 0]]))  # 9
