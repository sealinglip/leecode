#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-19 09:20:45
LastEditors: Thomas Young
LastEditTime: 2020-11-19 09:37:43
'''
#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 示例:
# 输入: [0, 1, 0, 3, 12]
# 输出: [1, 3, 12, 0, 0]
# 说明:

# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。

from typing import List
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums and len(nums):
            zeroCnt = 0
            ptr = 0
            dest = 0
            L = len(nums)
            while ptr < L:
                if nums[ptr] == 0:
                    zeroCnt += 1
                else:
                    if dest != ptr:
                        nums[dest] = nums[ptr]
                    dest += 1
                ptr += 1
            
            for i in range(dest, L):
                nums[i] = 0
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    list = [1]
    solution.moveZeroes(list)
    print(list)
    list = [0, 1, 0, 3, 12]
    solution.moveZeroes(list)
    print(list)
