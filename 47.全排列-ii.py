#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-27 18:30:16
LastEditors: Thomas Young
LastEditTime: 2020-09-18 09:25:14
'''
#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。

# 示例:
# 输入: [1, 1, 2]
# 输出:
# [
#     [1, 1, 2],
#     [1, 2, 1],
#     [2, 1, 1]
# ]
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        cnt = dict(Counter(nums))
        nums_len = len(nums)

        res = []
        permutation = []

        # 方法1：递归
        def permuteInner():
            if len(permutation) == nums_len:
                res.append(permutation[:])  # make a copy
                return
            for num in cnt:
                if cnt[num] > 0:
                    cnt[num] -= 1
                    permutation.append(num)
                    permuteInner()
                    permutation.pop()
                    cnt[num] += 1

        permuteInner()

        # 方法2：迭代
        
        return res
        

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.permuteUnique([1, 1, 2]))
