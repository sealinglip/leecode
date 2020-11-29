#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-09 21:28:16
LastEditors: Thomas Young
LastEditTime: 2020-09-20 20:33:18
'''
#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

# 示例:
# 输入:
# [
#     ["1", "0", "1", "0", "0"],
#     ["1", "0", "1", "1", "1"],
#     ["1", "1", "1", "1", "1"],
#     ["1", "0", "0", "1", "0"]
# ]
# 输出: 6
# 依赖84题的解法

from typing import List
# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        def largestRectangleArea(heights: List[int]) -> int:
            if not heights:
                return 0

            largest = 0
            stack = []
            for idx, height in enumerate(heights):
                if not stack or stack[-1][0] < height:
                    stack.append((height, idx))
                elif stack[-1][0] > height:
                    idx2 = 0
                    while stack and stack[-1][0] > height:
                        h2, idx2 = stack.pop()
                        area = h2 * (idx - idx2)
                        if area > largest:
                            largest = area
                    stack.append((height, idx2))
            idx = len(heights)
            while stack:
                h2, idx2 = stack.pop()
                area = h2 * (idx - idx2)
                if area > largest:
                    largest = area

            return largest

        N, M = len(matrix), len(matrix[0])
        lengths = [0] * N
        maximal = 0
        for col in range(M):
            for row in range(N):
                lengths[row] = lengths[row] + 1 if matrix[row][col] == '1' else 0
            largest = largestRectangleArea(lengths)
            if largest > maximal:
                maximal = largest
            
        return maximal

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximalRectangle([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]))

