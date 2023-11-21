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
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 子数组 是数组中的一个连续部分。

# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

# 示例 2：
# 输入：nums = [1]
# 输出：1

# 示例 3：
# 输入：nums = [5,4,-1,7,8]
# 输出：23
 

# 提示：
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。

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
    print(solution.maxSubArray([5,4,-1,7,8])) # 23
    print(solution.maxSubArray([1])) # 1
    print(solution.maxSubArray([-1])) # -1
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # 6
