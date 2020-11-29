#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-11 07:55:57
LastEditors: Thomas Young
LastEditTime: 2020-10-11 10:22:59
'''
#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，
# 使得两个子集的元素和相等。

# 注意:
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200

# 示例 1:
# 输入: [1, 5, 11, 5]
# 输出: true
# 解释: 数组可以分割成[1, 5, 5] 和[11].

# 示例 2:
# 输入: [1, 2, 3, 5]
# 输出: false
# 解释: 数组不能分割成两个元素和相等的子集.

from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 2:
            return False
        total = sum(nums)
        if total & 1: # total是奇数
            return False
        half = total >> 1 # 只要能从nums中找出数来凑成half即可

        maxVal = max(nums)
        if half < maxVal:
            return False
        dp = [False for _ in range(half + 1)] # dp[i] 表示能否用nums中的数字组合成i
        dp[0] = True
        accum = 0
        for n in nums:
            accum += n
            for t in range(min(half, accum), n - 1, -1):
                dp[t] |= dp[t - n]
                if dp[half]:
                    break
            else:
                continue
            break

        return dp[half]

        # 下面的方式时间会超标
        # cnt = Counter(nums)
        # keys = list(cnt.keys())
        # res = False
        # def resolve(i:int, target: int):
        #     nonlocal res
        #     if not target:
        #         res = True
        #     if res or i >= len(keys) or target < 0:
        #         return

        #     limit = min(cnt[keys[i]], target // keys[i]) + 1
        #     for j in range(limit):
        #         resolve(i + 1, target - j * keys[i])
        #         if res:
        #             return
            
        # resolve(0, half)
        # return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.canPartition([4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8,12,12,12,12,12,12,12,12,16,16,16,16,16,16,16,16,20,20,20,20,20,20,20,20,24,24,24,24,24,24,24,24,28,28,28,28,28,28,28,28,32,32,32,32,32,32,32,32,36,36,36,36,36,36,36,36,40,40,40,40,40,40,40,40,44,44,44,44,44,44,44,44,48,48,48,48,48,48,48,48,52,52,52,52,52,52,52,52,56,56,56,56,56,56,56,56,60,60,60,60,60,60,60,60,64,64,64,64,64,64,64,64,68,68,68,68,68,68,68,68,72,72,72,72,72,72,72,72,76,76,76,76,76,76,76,76,80,80,80,80,80,80,80,80,84,84,84,84,84,84,84,84,88,88,88,88,88,88,88,88,92,92,92,92,92,92,92,92,96,96,96,96,96,96,96,96,97,99]))
    print(solution.canPartition([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]))
    print(solution.canPartition([1, 5, 11, 5]))
    print(solution.canPartition([1, 2, 3, 5]))
