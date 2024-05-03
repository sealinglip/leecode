#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-04-24 20:51:00
LastEditors: Thomas Young
LastEditTime: 2021-04-24 21:16:37
'''
#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#
# 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
# 题目数据保证答案符合 32 位整数范围。

# 示例 1：
# 输入：nums = [1, 2, 3], target = 4
# 输出：7
# 解释：
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 请注意，顺序不同的序列被视作不同的组合。

# 示例 2：
# 输入：nums = [9], target = 3
# 输出：0
#  
# 提示：
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# nums 中的所有元素 互不相同
# 1 <= target <= 1000

# 进阶：如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？

from functools import cache
from typing import List
# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def combinationSum4Inner(t: int) -> int:
            sum = 0
            for n in nums:
                if n < t:
                    sum += combinationSum4Inner(t - n)
                elif n == t:
                    sum += 1
            return sum
        return combinationSum4Inner(target)
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum4([4, 2, 1], 32)) # 39882198
    print(solution.combinationSum4([1, 2, 3], 4)) # 7
    print(solution.combinationSum4([9], 3)) # 0
