#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-27 15:28:37
@LastEditors: Thomas Young
@LastEditTime: 2020-06-27 18:28:51
'''
#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列

# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

# 示例 1：
# 输入：nums = [1, 2, 3]
# 输出：[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# 示例 2：
# 输入：nums = [0, 1]
# 输出：[[0, 1], [1, 0]]

# 示例 3：
# 输入：nums = [1]
# 输出：[[1]]
#
from typing import List
# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        flag = [False for num in nums]  # 使用标志
        nums_len = len(nums)

        res = []
        permutation = []

        def permuteInner():
            if len(permutation) == nums_len:
                res.append(permutation[:])  # make a copy
                return
            for i in range(nums_len):
                if not flag[i]:
                    flag[i] = True
                    permutation.append(nums[i])
                    permuteInner()
                    permutation.pop()
                    flag[i] = False

        permuteInner()
        return res


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([1, 2, 3]))
