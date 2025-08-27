#
# @lc app=leetcode.cn id=3195 lang=python3
#
# [3195] 包含所有 1 的最小矩形面积 I
#
# https://leetcode.cn/problems/find-the-minimum-area-to-cover-all-ones-i/description/
#
# algorithms
# Medium (79.62%)
# Likes:    11
# Dislikes: 0
# Total Accepted:    15.6K
# Total Submissions: 19K
# Testcase Example:  '[[0,1,0],[1,0,1]]'
#
# 给你一个二维 二进制 数组 grid。请你找出一个边在水平方向和竖直方向上、面积 最小 的矩形，并且满足 grid 中所有的 1 都在矩形的内部。
# 返回这个矩形可能的 最小 面积。
# 
# 
# 示例 1：
# 输入： grid = [[0,1,0],[1,0,1]]
# 输出： 6
# 解释：
# 这个最小矩形的高度为 2，宽度为 3，因此面积为 2 * 3 = 6。
# 
# 示例 2：
# 输入： grid = [[0,0],[1,0]]
# 输出： 1
# 解释：
# 这个最小矩形的高度和宽度都是 1，因此面积为 1 * 1 = 1。
# 
# 
# 提示：
# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] 是 0 或 1。
# 输入保证 grid 中至少有一个 1 。
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 求出为1的单元格的坐标边界
        lb, rb = n-1, 0
        ub, bb = m-1, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    lb = min(lb, j)
                    rb = max(rb, j)
                    ub = min(ub, i)
                    bb = max(bb, i)
        
        return (rb - lb + 1) * (bb - ub + 1)
        
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumArea([[0],[1]])) # 1
    print(solution.minimumArea([[0,1,0],[1,0,1]])) # 6
    print(solution.minimumArea([[0,0],[1,0]])) # 1
