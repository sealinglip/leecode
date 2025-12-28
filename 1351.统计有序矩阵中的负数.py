#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#
# https://leetcode.cn/problems/count-negative-numbers-in-a-sorted-matrix/description/
#
# algorithms
# Easy (74.79%)
# Likes:    204
# Dislikes: 0
# Total Accepted:    73.2K
# Total Submissions: 97.1K
# Testcase Example:  '[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]'
#
# 给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非严格递减顺序排列。 请你统计并返回 grid 中 负数 的数目。
# 
# 
# 示例 1：
# 输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# 输出：8
# 解释：矩阵中共有 8 个负数。
# 
# 示例 2：
# 输入：grid = [[3,2],[1,0]]
# 输出：0
# 
# 
# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
# 
# 
# 进阶：你可以设计一个时间复杂度为 O(n + m) 的解决方案吗？
# 
#

from bisect import bisect_right
from typing import List

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        pivotPos = n # 第一个小于0的元素位置
        res = 0
        for row in grid:
            pivotPos = bisect_right(row, 0, 0, pivotPos, key=lambda x : -x)
            res += n - pivotPos

        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])) # 8
    print(solution.countNegatives([[3,2],[1,0]])) # 0
