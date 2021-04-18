#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-15 05:46:28
@LastEditors: Thomas Young
@LastEditTime: 2020-06-15 05:51:35
'''
#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#
from typing import List
# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length, deleted = len(nums), 0

        preVal = None
        for i in range(length - 1, -1, -1):
            if nums[i] == preVal:
                del nums[i]
                deleted += 1
            else:
                preVal = nums[i]

        return length - deleted
# @lc code=end
