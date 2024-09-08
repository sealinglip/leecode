# 给你一个由 正整数 组成、大小为 m x n 的矩阵 grid。你可以从矩阵中的任一单元格移动到另一个位于正下方或正右侧的任意单元格（不必相邻）。从值为 c1 的单元格移动到值为 c2 的单元格的得分为 c2 - c1 。
# 你可以从 任一 单元格开始，并且必须至少移动一次。
# 返回你能得到的 最大 总得分。

# 示例 1：
# 输入：grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]
# 输出：9
# 解释：从单元格 (0, 1) 开始，并执行以下移动：
# - 从单元格 (0, 1) 移动到 (2, 1)，得分为 7 - 5 = 2 。
# - 从单元格 (2, 1) 移动到 (2, 2)，得分为 14 - 7 = 7 。
# 总得分为 2 + 7 = 9 。

# 示例 2：
# 输入：grid = [[4,3,2],[3,2,1]]
# 输出：-1
# 解释：从单元格 (0, 0) 开始，执行一次移动：从 (0, 0) 到 (0, 1) 。得分为 3 - 4 = -1 。

# 提示：
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 10^5
# 1 <= grid[i][j] <= 10^5

from math import inf
from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        presumRow = [[0] * n for _ in range(m)]
        presumCol = [[0] * n for _ in range(m)]
        # 记dp(i,j)为以(i,j)位置结束的最大得分
        dp = [[-inf] * n for _ in range(m)]

        res = -inf
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] = max(dp[i][j], grid[i][j] + presumCol[i-1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], grid[i][j] + presumRow[i][j-1])
                
                res = max(res, dp[i][j])
                presumCol[i][j] = presumRow[i][j] = max(dp[i][j], 0) - grid[i][j]
                if i > 0:
                    presumCol[i][j] = max(presumCol[i][j], presumCol[i-1][j])
                if j > 0:
                    presumRow[i][j] = max(presumRow[i][j], presumRow[i][j-1])
                    
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxScore([[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]])) # 9
    print(solution.maxScore([[4,3,2],[3,2,1]])) # -1
    