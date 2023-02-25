#
# @lc app=leetcode.cn id=1139 lang=python3
#
# [1139] 最大的以 1 为边界的正方形
#
# 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。


# 示例 1：
# 输入：grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# 输出：9

# 示例 2：
# 输入：grid = [[1, 1, 0, 0]]
# 输出：1

# 提示：
# 1 <= grid.length <= 100
# 1 <= grid[0].length <= 100
# grid[i][j] 为 0 或 1

# 复习

from typing import List
# @lc code=start


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        left = [[0] * (n + 1) for _ in range(m + 1)]
        up = [[0] * (n + 1) for _ in range(m + 1)]
        maxBorder = 0
        # 动规
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i-1][j-1]:
                    left[i][j] = left[i][j-1] + 1
                    up[i][j] = up[i-1][j] + 1
                    border = min(left[i][j], up[i][j])
                    while left[i - border + 1][j] < border or up[i][j - border + 1] < border:
                        border -= 1
                    maxBorder = max(maxBorder, border)

        return maxBorder ** 2


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.largest1BorderedSquare(
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # 9
    print(solution.largest1BorderedSquare([[1, 1, 0, 0]]))  # 1
