#
# @lc app=leetcode.cn id=1895 lang=python3
#
# [1895] 最大的幻方
#
# https://leetcode.cn/problems/largest-magic-square/description/
#
# algorithms
# Medium (58.43%)
# Likes:    34
# Dislikes: 0
# Total Accepted:    7.3K
# Total Submissions: 11.3K
# Testcase Example:  '[[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]'
#
# 一个 k x k 的 幻方 指的是一个 k x k 填满整数的方格阵，且每一行、每一列以及两条对角线的和 全部相等 。幻方中的整数 不需要互不相同
# 。显然，每个 1 x 1 的方格都是一个幻方。
# 
# 给你一个 m x n 的整数矩阵 grid ，请你返回矩阵中 最大幻方 的 尺寸 （即边长 k）。
# 
# 
# 示例 1：
# 输入：grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
# 输出：3
# 解释：最大幻方尺寸为 3 。
# 每一行，每一列以及两条对角线的和都等于 12 。
# - 每一行的和：5+1+6 = 5+4+3 = 2+7+3 = 12
# - 每一列的和：5+5+2 = 1+4+7 = 6+3+3 = 12
# - 对角线的和：5+4+3 = 6+4+2 = 12
# 
# 示例 2：
# 输入：grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
# 输出：2
# 
# 
# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 10^6
# 
# 
#

from itertools import accumulate
from typing import List
# @lc code=start
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        # 求出行和列的前缀和，再暴力求解
        m, n = len(grid), len(grid[0])

        # 行前缀和
        rowPreSum = [[0] + list(accumulate(row)) for row in grid]
        
        # 列前缀和
        colPreSum = [[0] + list(accumulate(col)) for col in zip(*grid)]

        def check(i: int, j: int, size: int) -> bool:
            '''
            检查以(i, j)为左上角，边长为size的方格阵是否为幻方阵
            '''
            targetSum = rowPreSum[i][j + edge] - rowPreSum[i][j] # 拿第一行做样本，求出目标和
            # 检查每一行
            for r in range(i + 1, i + edge):
                if rowPreSum[r][j + edge] - rowPreSum[r][j] != targetSum:
                    return False
            # 检查每一列
            for c in range(j, j + edge):
                if colPreSum[c][i + edge] - colPreSum[c][i] != targetSum:
                    return False
            # 检查对角线
            d1 = d2 = 0
            for k in range(edge):
                d1 += grid[i + k][j + k]
                d2 += grid[i + k][j + edge - k - 1]
            if d1 != targetSum or d2 != targetSum:
                return False

            return True


        for edge in range(min(m, n), 1, -1): # 从最大可能往下尝试，减少计算量
            # 左上角位置(i, j)
            for i in range(m - edge + 1):
                for j in range(n - edge + 1):
                    if check(i, j, edge):
                        return edge
        return 1
                    
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.largestMagicSquare([[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]])) # 3
    print(solution.largestMagicSquare([[5,1,3,1],[9,3,3,1],[1,3,3,8]])) # 2
