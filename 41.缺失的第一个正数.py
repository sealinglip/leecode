#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-16 23:27:22
LastEditors: Thomas Young
LastEditTime: 2020-09-21 09:00:06
'''
#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

# 示例 1:
# 输入: [1, 2, 0]
# 输出: 3

# 示例 2:
# 输入: [3, 4, -1, 1]
# 输出: 2

# 示例 3:
# 输入: [7, 8, 9, 11, 12]
# 输出: 1

# 提示：
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。

from typing import List

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or 1 not in nums:
            return 1
        elif len(nums) == 1:
            return 2

        n = len(nums)
        # 先处理负值和0
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = 1

        # 遍历标记
        for i in range(n):
            a = abs(nums[i])
            if a > n:
                continue
            a = a if a < n else 0
            nums[a] = -abs(nums[a])

        for i in range(1, n):
            if nums[i] > 0:
                return i

        return n if nums[0] > 0 else n + 1
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.firstMissingPositive([0, -1, 3, 1]))
    print(solution.firstMissingPositive([1, 1000]))
    print(solution.firstMissingPositive([1, 2, 0]))
