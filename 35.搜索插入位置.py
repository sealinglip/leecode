#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-20 14:22:25
@LastEditors: Thomas Young
@LastEditTime: 2020-06-20 14:24:29
'''
#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 二分查找
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            mid_val = nums[mid]

            if mid_val < target:
                low = mid + 1
            elif mid_val > target:
                high = mid - 1
            else:
                return mid
        return low
# @lc code=end

