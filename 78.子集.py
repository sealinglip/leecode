#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-20 08:32:29
LastEditors: Thomas Young
LastEditTime: 2020-09-20 08:48:12
'''
#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例:
# 输入: nums = [1, 2, 3]
# 输出:
# [
#     [3],
#     [1],
#     [2],
#     [1, 2, 3],
#     [1, 3],
#     [2, 3],
#     [1, 2],
#     []
# ]

from typing import List
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        l = len(nums)
        res = []
        flag = [False] * l
        def enum(i):
            if i == l:
                res.append([num for idx, num in enumerate(nums) if flag[idx]])
            else:
                enum(i + 1)
                flag[i] = True
                enum(i + 1)
                flag[i] = False

        enum(0)
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.subsets([1, 2]))
    print(solution.subsets([1, 2, 3]))
