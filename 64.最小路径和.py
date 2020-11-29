#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-20 20:34:46
LastEditors: Thomas Young
LastEditTime: 2020-09-20 20:45:40
'''
#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。

# 示例:
# 输入:
# [
#     [1, 3, 1],
#     [1, 5, 1],
#     [4, 2, 1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。

from typing import List
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        # 典型DP
        N, M = len(grid), len(grid[0]) # grid的维度值
        minPathSum = grid[0][:]
        for col in range(1, M):
            minPathSum[col] += minPathSum[col - 1]
        for row in range(1, N):
            minPathSum[0] += grid[row][0]
            for col in range(1, M):
                minPathSum[col] = min(minPathSum[col - 1], minPathSum[col]) + grid[row][col]
        
        return minPathSum[-1]
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
