#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-15 07:55:58
LastEditors: Thomas Young
LastEditTime: 2020-09-20 20:16:58
'''
#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

# 求在该柱状图中，能够勾勒出来的矩形的最大面积。


# 示例 1:
# 输入：heights = [2, 1, 5, 6, 2, 3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10

# 示例 2：
# 输入： heights = [2, 4]
# 输出： 4


# 提示：
# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4

# Hard

from typing import List
# @lc code=start


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))
