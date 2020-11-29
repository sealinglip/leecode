#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-16 22:06:27
@LastEditors: Thomas Young
@LastEditTime: 2020-06-16 22:09:09
'''
#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        
        return len(nums)
# @lc code=end

