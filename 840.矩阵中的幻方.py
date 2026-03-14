#
# @lc app=leetcode.cn id=840 lang=python3
#
# [840] 矩阵中的幻方
#
# https://leetcode.cn/problems/magic-squares-in-grid/description/
#
# algorithms
# Medium (37.62%)
# Likes:    78
# Dislikes: 0
# Total Accepted:    15.5K
# Total Submissions: 39.5K
# Testcase Example:  '[[4,3,8,4],[9,5,1,9],[2,7,6,2]]'
#
# 3 x 3 的幻方是一个填充有 从 1 到 9  的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。
# 
# 给定一个由整数组成的row x col 的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？
# 
# 注意：虽然幻方只能包含 1 到 9 的数字，但 grid 可以包含最多15的数字。
# 
# 
# 示例 1：
# 输入: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# 输出: 1
# 解释: 
# 下面的子矩阵是一个 3 x 3 的幻方：
# 而这一个不是：
# 总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
# 
# 示例 2:
# 输入: grid = [[8]]
# 输出: 0
# 
# 
# 提示:
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 10
# 0 <= grid[i][j] <= 15
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        if row < 3 or col < 3:
            return 0
        
        def checkMagic(r: int, c: int) -> bool:
            if grid[r][c] != 5:
                # 三阶幻方中心元素只能是5
                return False
            return grid[r-1][c-1] + grid[r-1][c] + grid[r-1][c+1] == 15 \
                and grid[r][c-1] + grid[r][c+1] == 10 \
                and grid[r+1][c-1] + grid[r+1][c] + grid[r+1][c+1] == 15 \
                and grid[r-1][c-1] + grid[r][c-1] + grid[r+1][c-1] == 15 \
                and grid[r-1][c+1] + grid[r][c+1] + grid[r+1][c+1] == 15 \
                and grid[r-1][c] + grid[r+1][c] == 10 \
                and grid[r-1][c-1] + grid[r+1][c+1] == 10 \
                and grid[r-1][c+1] + grid[r+1][c-1] == 10 \
                and sorted([grid[r-1][c-1], grid[r-1][c], grid[r-1][c+1], grid[r][c-1], grid[r][c], grid[r][c+1], grid[r+1][c-1], grid[r+1][c], grid[r+1][c+1]]) == list(range(1, 10))
        
        # 暴力
        res = 0
        for r in range(1, row-1):
            for c in range(1, col-1):
                if checkMagic(r, c):
                    res += 1

        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.numMagicSquaresInside([[5,5,5],[5,5,5],[5,5,5]])) # 0
    print(solution.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]])) # 1
    print(solution.numMagicSquaresInside([[8]])) # 0
