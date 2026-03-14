# 给你一个 m x n 的二维整数数组 grid 和一个整数 k。你从左上角的单元格 (0, 0) 出发，目标是到达右下角的单元格 (m - 1, n - 1)。
# 有两种移动方式可用：
# 普通移动：你可以从当前单元格 (i, j) 向右或向下移动，即移动到 (i, j + 1)（右）或 (i + 1, j)（下）。成本为目标单元格的值。
# 传送：你可以从任意单元格 (i, j) 传送到任意满足 grid[x][y] <= grid[i][j] 的单元格 (x, y)；此移动的成本为 0。你最多可以传送 k 次。
# 返回从 (0, 0) 到达单元格 (m - 1, n - 1) 的 最小 总成本。


# 示例 1:
# 输入: grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2
# 输出: 7
# 解释:
# 我们最初在 (0, 0)，成本为 0。
# 当前位置	移动	新位置	总成本
# (0, 0)	向下移动	(1, 0)	0 + 2 = 2
# (1, 0)	向右移动	(1, 1)	2 + 5 = 7
# (1, 1)	传送到 (2, 2)	(2, 2)	7 + 0 = 7
# 到达右下角单元格的最小成本是 7。

# 示例 2:
# 输入: grid = [[1,2],[2,3],[3,4]], k = 1
# 输出: 9
# 解释:
# 我们最初在 (0, 0)，成本为 0。
# 当前位置	移动	新位置	总成本
# (0, 0)	向下移动	(1, 0)	0 + 2 = 2
# (1, 0)	向右移动	(1, 1)	2 + 3 = 5
# (1, 1)	向下移动	(2, 1)	5 + 4 = 9
# 到达右下角单元格的最小成本是 9。
 

# 提示:
# 2 <= m, n <= 80
# m == grid.length
# n == grid[i].length
# 0 <= grid[i][j] <= 10^4
# 0 <= k <= 10


from math import inf
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        cells = [(i, j) for i in range(m) for j in range(n)]
        cells.sort(key=lambda c: grid[c[0]][c[1]]) # 将cells按值升序排序

        # 动规
        # 记dp(t, i, j)为使用t次传送，从(i,j)到(m-1, n-1)的最小成本
        # dp(t, i, j) = min(dp(t, i+1, j)+grid[i+1][j], dp(t, i, j+1)+grid[i][j+1])  —— 不使用传送时
        # dp(t, i, j) = min(dp(t-1, x, y) for x, y if grid[x][y] <= grid[i][j]) —— 使用传送时
        # 因为dp(t, i, j)只依赖dp(t-1, *, *)，状态矩阵可以压缩为二维
        dp = [[inf] * n for _ in range(m)]
        for t in range(k+1):
            minCost = inf
            j = 0
            for i in range(len(cells)):
                minCost = min(minCost, dp[cells[i][0]][cells[i][1]])
                if i + 1 < len(cells) and grid[cells[i][0]][cells[i][1]] == grid[cells[i + 1][0]][cells[i + 1][1]]:
                    i += 1
                    continue
                for r in range(j, i + 1):
                    dp[cells[r][0]][cells[r][1]] = minCost
                j = i + 1
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if i == m - 1 and j == n - 1:
                        dp[i][j] = 0
                        continue
                    if i != m - 1:
                        dp[i][j] = min(dp[i][j], dp[i + 1][j] + grid[i + 1][j])
                    if j != n - 1:
                        dp[i][j] = min(dp[i][j], dp[i][j + 1] + grid[i][j + 1])
        return dp[0][0]
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.minCost([[1,3,3],[2,5,4],[4,3,5]], 2)) # 7
    print(solution.minCost([[1,2],[2,3],[3,4]], 1)) # 9
