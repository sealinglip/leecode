#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-08-28 09:35:21
LastEditors: Thomas Young
LastEditTime: 2020-08-28 09:45:13
'''
#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:

# 输入: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 输出: 6
# 解释: 连续子数组[4, -1, 2, 1] 的和最大，为 6。
# 进阶:

# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 时间复杂度O(n)
        # 累计，记录最小值和当前值
        sum, min_sum, max_sub = 0, 0, float("-inf")

        for n in nums:
            sum += n
            max_sub = max(max_sub, sum - min_sum)
            min_sum = min(min_sum, sum)

        return max_sub
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-1]))
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
