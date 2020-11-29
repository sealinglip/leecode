#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-06-10 22:27:31
LastEditors: Thomas Young
LastEditTime: 2020-09-02 16:05:00
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# 给定一个整数数组 nums 和一个目标值  target，请你在该数组中找出和为目标值的那 
# 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回[0, 1]

from typing import List
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            d[target - num] = i
        return []
            
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
