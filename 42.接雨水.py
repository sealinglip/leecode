#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-17 11:16:53
@LastEditors: Thomas Young
@LastEditTime: 2020-06-17 16:19:19
'''
#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


# 示例 1：
# 输入：height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# 输出：6
# 解释：上面是由数组[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

# 示例 2：
# 输入：height = [4, 2, 0, 3, 2, 5]
# 输出：9


# 提示：
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5

# Hard
from typing import List
# @lc code=start


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # 遍历，总是保存到当前位置的前最高点和位置，以及累计的装水
        # 由两侧往中间走，直到相遇，相遇之后，取边界较低的一侧，前行至较高的一侧
        leftHighest, leftPos, rightHighest, rightPos, totalAccum, currLeftAccum, currRightAccum = \
            height[0], 0, height[-1], len(height) - 1, 0, 0, 0
        l, r = leftPos + 1, rightPos - 1
        while l < r:
            if height[l] >= leftHighest:
                leftHighest = height[l]
                leftPos = l
                totalAccum += currLeftAccum
                currLeftAccum = 0
            else:
                currLeftAccum += leftHighest - height[l]
            l += 1
            if height[r] >= rightHighest:
                rightHighest = height[r]
                rightPos = r
                totalAccum += currRightAccum
                currRightAccum = 0
            else:
                currRightAccum += rightHighest - height[r]
            r -= 1

        if l == r and height[l] >= leftHighest and height[l] >= rightHighest:  # 相遇到一个更高点（比两侧都高）
            totalAccum += currLeftAccum + currRightAccum
        elif leftHighest > rightHighest:  # 右边继续往左边推
            while r > leftPos:
                if height[r] >= rightHighest:
                    rightHighest = height[r]
                    rightPos = r
                    totalAccum += currRightAccum
                    currRightAccum = 0
                else:
                    currRightAccum += rightHighest - height[r]
                r -= 1
            totalAccum += currRightAccum
        else:  # 左边往右边推
            while l < rightPos:
                if height[l] >= leftHighest:
                    leftHighest = height[l]
                    leftPos = l
                    totalAccum += currLeftAccum
                    currLeftAccum = 0
                else:
                    currLeftAccum += leftHighest - height[l]
                l += 1
            totalAccum += currLeftAccum

        return totalAccum

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([0]))
    print(solution.trap([8, 0, 8, 1, 0, 9, 6, 0, 7, 2, 5]))
    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
