#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-07-09 11:18:20
@LastEditors: Thomas Young
@LastEditTime: 2020-07-09 11:22:20
'''
#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 网格中的障碍物和空位置分别用 1 和 0 来表示。

# 说明：m 和 n 的值均不超过 100。
# 示例 1:
# 输入:
# [
#     [0, 0, 0],
#     [0, 1, 0],
#     [0, 0, 0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        cache = [0 for i in range(m)]

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j]:
                    cache[j] = 0
                elif i == 0 and j == 0:
                    cache[j] = 1
                elif j:
                    cache[j] += cache[j - 1]

        return cache[-1]

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
