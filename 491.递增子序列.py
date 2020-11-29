#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-08-25 09:02:42
LastEditors: Thomas Young
LastEditTime: 2020-08-26 08:52:56
'''
#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
# 示例:
# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7],
#     [6, 7], [6, 7, 7], [7, 7], [4, 7, 7]]
# 说明:
# 1. 给定数组的长度不会超过15。
# 2. 数组中的整数范围是[-100, 100]。
# 3. 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
#

from typing import List
# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 2: # 数组为空或数组长度不够
            return []
        
        # 方法1：DP + 哈希去重
        # res = {(nums[0], )} # 初始
        # for num in nums[1:]:
        #     res.update({r + (num, ) for r in res if r[-1] <= num})
        #     res.add((num, ))

        # return [list(r) for r in res if len(r) > 1]

        # 方法2：DFS + 去重
        res = []
        def dfs(arr: List[int], tmp: List[int]):
            if len(tmp) > 1:
                res.append(tmp)
            handled = set() # 记录处理过的数字
            for idx, num in enumerate(arr):
                if num in handled:
                    continue
                elif not tmp or tmp[-1] <= num:
                    handled.add(num)
                    dfs(arr[idx + 1:], tmp + [num])
        dfs(nums, [])
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    # print(solution.findSubsequences([4, 6, 7, 7]))
    print(solution.findSubsequences(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]))

    pass

