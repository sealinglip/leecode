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
#
from typing import List
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        flag = [False for num in nums] #使用标志
        nums_len = len(nums)

        res = []
        permutation = []
        def permuteInner():
            if len(permutation) == nums_len:
                res.append(permutation[:]) # make a copy
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
    print(solution.permute([1,2,3]))
