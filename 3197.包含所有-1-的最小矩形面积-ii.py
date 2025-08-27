#
# @lc app=leetcode.cn id=3197 lang=python3
#
# [3197] 包含所有 1 的最小矩形面积 II
#
# https://leetcode.cn/problems/find-the-minimum-area-to-cover-all-ones-ii/description/
#
# algorithms
# Hard (34.14%)
# Likes:    30
# Dislikes: 0
# Total Accepted:    7K
# Total Submissions: 13.1K
# Testcase Example:  '[[1,0,1],[1,1,1]]'
#
# 给你一个二维 二进制 数组 grid。你需要找到 3 个 不重叠、面积 非零 、边在水平方向和竖直方向上的矩形，并且满足 grid 中所有的 1
# 都在这些矩形的内部。
# 
# 返回这些矩形面积之和的 最小 可能值。
# 
# 注意，这些矩形可以相接。
# 
# 
# 示例 1：
# 输入： grid = [[1,0,1],[1,1,1]]
# 输出： 5
# 解释：
# 位于 (0, 0) 和 (1, 0) 的 1 被一个面积为 2 的矩形覆盖。
# 位于 (0, 2) 和 (1, 2) 的 1 被一个面积为 2 的矩形覆盖。
# 位于 (1, 1) 的 1 被一个面积为 1 的矩形覆盖。
# 
# 示例 2：
# 输入： grid = [[1,0,1,0],[0,1,0,1]]
# 输出： 5
# 解释：
# 位于 (0, 0) 和 (0, 2) 的 1 被一个面积为 3 的矩形覆盖。
# 位于 (1, 1) 的 1 被一个面积为 1 的矩形覆盖。
# 位于 (1, 3) 的 1 被一个面积为 1 的矩形覆盖。
# 
# 
# 提示：
# 1 <= grid.length, grid[i].length <= 30
# grid[i][j] 是 0 或 1。
# 输入保证 grid 中至少有三个 1 。
# 
# 复习
#

from math import inf
from typing import List
# @lc code=start
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        return min(self.solve(grid), self.solve(self.rotate90(grid)))

    def rotate90(self, grid: List[List[int]]) -> List[List[int]]:
        '''
        将矩阵顺时针转90°
        '''
        return list(zip(*reversed(grid)))
    
    def solve(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def minimumArea(a: List[List[int]]) -> List[List[int]]:
            m, n = len(a), len(a[0])
            # 记dp[i][j]表示左上角为(0,0)右下角为(i-1,j-1) (包含）的子矩阵中包含所有1的最小矩形面积
            dp = [[0] * (n+1) for _ in range(m+1)]
            border = [(-1, 0, 0)] * n
            for i, row in enumerate(a):
                left, right = -1, 0
                for j, x in enumerate(row):
                    if x:
                        if left < 0:
                            left = j
                        right = j
                    pre_top, pre_left, pre_right = border[j]
                    if left < 0:  # 这一排目前全是 0
                        dp[i + 1][j + 1] = dp[i][j + 1]  # 等于上面的结果
                    elif pre_top < 0:  # 这一排有 1，上面全是 0
                        dp[i + 1][j + 1] = right - left + 1
                        border[j] = (i, left, right)
                    else:  # 这一排有 1，上面也有 1
                        l = min(pre_left, left)
                        r = max(pre_right, right)
                        dp[i + 1][j + 1] = (r - l + 1) * (i - pre_top + 1)
                        border[j] = (pre_top, l, r)
            return dp

        # 预处理每一行最左最右 1 的列号，用于中间区域最小矩形面积的计算
        lr = [None] * m
        for i in range(m):
            l, r = -1, 0
            for j in range(n):
                if grid[i][j]:
                    if l < 0:
                        l = j
                    r = j
            lr[i] = (l, r)

        # lt[i+1][j+1] = 包含【左上角为 (0,0) 右下角为 (i,j) 的子矩形】中的所有 1 的最小矩形面积
        lt = minimumArea(grid)
        grid = self.rotate90(grid)
        # lb[i][j+1] = 包含【左下角为 (m-1,0) 右上角为 (i,j) 的子矩形】中的所有 1 的最小矩形面积
        lb = self.rotate90(self.rotate90(self.rotate90(minimumArea(grid))))
        grid = self.rotate90(grid)
        # rb[i][j] = 包含【右下角为 (m-1,n-1) 左上角为 (i,j) 的子矩形】中的所有 1 的最小矩形面积
        rb = self.rotate90(self.rotate90(minimumArea(grid)))
        grid = self.rotate90(grid)
        # rt[i+1][j] = 包含【右上角为 (0,n-1) 左下角为 (i,j) 的子矩形】中的所有 1 的最小矩形面积
        rt = self.rotate90(minimumArea(grid))

        ans = inf
        if m >= 3:
            for i in range(1, m):
                left, right, top, bottom = n, -1, m, -1
                for j in range(i + 1, m):
                    l, r = lr[j - 1]
                    if l >= 0:
                        left = min(left, l)
                        right = max(right, r)
                        top = min(top, j - 1)
                        bottom = j - 1
                    # 图片上左
                    ans = min(ans, lt[i][n] + (right - left + 1) * (bottom - top + 1) + lb[j][n])

        if m >= 2 and n >= 2:
            for i in range(1, m):
                for j in range(1, n):
                    # 图片上中
                    ans = min(ans, lt[i][n] + lb[i][j] + rb[i][j])
                    # 图片上右
                    ans = min(ans, lt[i][j] + rt[i][j] + lb[i][n])
        return ans
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumSum([[1,0,1],[1,1,1]])) # 5
    print(solution.minimumSum([[1,0,1,0],[0,1,0,1]])) # 5