#
# @lc app=leetcode.cn id=1975 lang=python3
#
# [1975] 最大方阵和
#
# https://leetcode.cn/problems/maximum-matrix-sum/description/
#
# algorithms
# Medium (43.31%)
# Likes:    32
# Dislikes: 0
# Total Accepted:    8.6K
# Total Submissions: 18.3K
# Testcase Example:  '[[1,-1],[-1,1]]'
#
# 给你一个 n x n 的整数方阵 matrix 。你可以执行以下操作 任意次 ：
# 选择 matrix 中 相邻 两个元素，并将它们都 乘以 -1 。
# 如果两个元素有 公共边 ，那么它们就是 相邻 的。
# 你的目的是 最大化 方阵元素的和。请你在执行以上操作之后，返回方阵的 最大 和。
# 
# 
# 示例 1：
# 输入：matrix = [[1,-1],[-1,1]]
# 输出：4
# 解释：我们可以执行以下操作使和等于 4 ：
# - 将第一行的 2 个元素乘以 -1 。
# - 将第一列的 2 个元素乘以 -1 。
# 
# 示例 2：
# 输入：matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
# 输出：16
# 解释：我们可以执行以下操作使和等于 16 ：
# - 将第二行的最后 2 个元素乘以 -1 。
# 
# 
# 提示：
# n == matrix.length == matrix[i].length
# 2 <= n <= 250
# -10^5 <= matrix[i][j] <= 10^5
# 
# 
#

from math import inf
from typing import List
# @lc code=start
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # 任意两个元素都可以在有限次翻转之后同时改变正负号
        # # 对所有元素排序
        # elements = [v for row in matrix for v in row]
        # elements.sort()
        # res = sum(elements)
        # i = 0
        # n = len(elements)
        # while i < n and elements[i] < 0:
        #     if i < n - 1 and (c := elements[i] + elements[i+1]) < 0:
        #         res -= c << 1
        #     i += 2
        # return res

        res = 0
        negCnt = 0 # 记录负数个数
        minAbs = inf # 记录最小绝对值
        for row in matrix:
            for v in row:
                minAbs = min(minAbs, abs(v))
                res += abs(v)
                if v < 0:
                    negCnt += 1
        
        if negCnt & 1 == 0:
            return res
        else:
            return res - (minAbs << 1)
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxMatrixSum([[1,-1],[-1,1]])) # 4
    print(solution.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]])) # 16
