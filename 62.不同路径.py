#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-07-09 11:11:15
@LastEditors: Thomas Young
@LastEditTime: 2020-07-09 11:17:55
'''
#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？
# 示例 1:

# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右

# 示例 2:

# 输入: m = 7, n = 3
# 输出: 28

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [1 for i in range(m)]
        for i in range(1, n):
            for j in range(m):
                if j == 0:
                    cache[j] = 1
                else:
                    cache[j] += cache[j - 1]
        return cache[-1]

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(7, 3))
