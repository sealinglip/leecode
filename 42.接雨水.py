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

        if l == r and height[l] >= leftHighest and height[l] >= rightHighest: #相遇到一个更高点（比两侧都高）
            totalAccum += currLeftAccum + currRightAccum
        elif leftHighest > rightHighest: # 右边继续往左边推
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
        else: # 左边往右边推
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
