#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-08 22:23:08
LastEditors: Thomas Young
LastEditTime: 2020-10-08 22:53:14
'''
#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例:

# 输入: [1, 2, 2]
# 输出:
# [
#     [2],
#     [1],
#     [1, 2, 2],
#     [2, 2],
#     [1, 2],
#     []
# ]

from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        cnt = Counter(nums)
        key = list(cnt.keys())
        l = len(key)
        res = []

        def enum(i, arr):
            if i == l:
                res.append(arr)
            else:
                c = cnt[key[i]] # 第i个字符的个数
                for j in range(c + 1):
                    enum(i + 1, arr + j * [key[i]])

        enum(0, [])
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.subsetsWithDup([1, 2, 2]))
