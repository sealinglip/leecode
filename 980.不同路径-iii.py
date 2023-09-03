#
# @lc app=leetcode.cn id=980 lang=python3
#
# [980] 不同路径 III
#
# 在二维网格 grid 上，有 4 种类型的方格：

# 1 表示起始方格。且只有一个起始方格。
# 2 表示结束方格，且只有一个结束方格。
# 0 表示我们可以走过的空方格。
# -1 表示我们无法跨越的障碍。
# 返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。

# 每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。


# 示例 1：
# 输入：[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
# 输出：2
# 解释：我们有以下两条路径：
# 1. (0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1,
#                                             2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2)
# 2. (0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0,
#                                             1), (0, 2), (0, 3), (1, 3), (1, 2), (2, 2)

# 示例 2：
# 输入：[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
# 输出：4
# 解释：我们有以下四条路径：
# 1. (0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1,
#                                             2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)
# 2. (0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (2,
#                                             1), (2, 2), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3)
# 3. (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1,
#                                             2), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)
# 4. (0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0,
#                                             1), (0, 2), (0, 3), (1, 3), (1, 2), (2, 2), (2, 3)

# 示例 3：
# 输入：[[0, 1], [2, 0]]
# 输出：0
# 解释：
# 没有一条路能完全穿过每一个空的方格一次。
# 请注意，起始和结束方格可以位于网格中的任意位置。


# 提示：
# 1 <= grid.length * grid[0].length <= 20

# Hard
# 复习

from functools import cache
from typing import List
# @lc code=start


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        si = sj = st = 0  # 分别记录起点坐标（si, sj）和待经过的点（st）
        for i in range(m):
            for j in range(n):
                if grid[i][j] in [0, 2]:
                    st |= 1 << (i * n + j)  # 待经过的点 mask
                elif grid[i][j] == 1:
                    si, sj = i, j

        @cache
        def dp(i: int, j: int, st: int) -> int:
            '''
            求从 (i, j) 点出发，待经过点的mask为st的所有合法路径数
            '''
            if grid[i][j] == 2:
                if st == 0:
                    return 1
                return 0
            res = 0
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (st & (1 << (ni * n + nj))):
                    res += dp(ni, nj, st ^ (1 << (ni * n + nj)))
            return res

        return dp(si, sj, st)


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePathsIII(
        [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))  # 2
    print(solution.uniquePathsIII(
        [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))  # 4
    print(solution.uniquePathsIII([[0, 1], [2, 0]]))  # 0
