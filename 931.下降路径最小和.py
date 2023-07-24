#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 下降路径最小和
#
# 给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。

# 下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置(row, col) 的下一个元素应当是(row + 1, col - 1)、(row + 1, col) 或者(row + 1, col + 1) 。


# 示例 1：
# 输入：matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
# 输出：13
# 解释：如图所示，为和最小的两条下降路径

# 示例 2：
# 输入：matrix = [[-19, 57], [-40, -5]]
# 输出：- 59
# 解释：如图所示，为和最小的下降路径


# 提示：
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100

from typing import List
# @lc code=start


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = list(matrix[0])

        for i in range(1, n):
            row = matrix[i]
            newdp = [0] * n
            newdp[0] = min(dp[0], dp[1]) + row[0]
            for j in range(1, n - 1):
                newdp[j] = min(dp[j-1], dp[j], dp[j+1]) + row[j]
            newdp[n-1] = min(dp[n-1], dp[n-2]) + row[n-1]
            dp = newdp

        return min(dp)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))  # 13
    print(solution.minFallingPathSum([[-19, 57], [-40, -5]]))  # -59
