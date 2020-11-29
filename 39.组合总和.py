#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-21 19:20:01
LastEditors: Thomas Young
LastEditTime: 2020-09-09 09:13:50
'''
#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中
# 所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。
# 说明：
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。

# 示例 1:
# 输入: candidates = [2, 3, 6, 7], target = 7,
# 所求解集为:
# [
#     [7],
#     [2, 2, 3]
# ]

# 示例 2:
# 输入: candidates = [2, 3, 5], target = 8,
# 所求解集为:
# [
#     [2, 2, 2, 2],
#     [2, 3, 3],
#     [3, 5]
# ]

from typing import List
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 方法1：动态规划
        # dp = {i: [] for i in range(target+1)} # dp[i] 代表数字i可以被分解为candidates的解集

        # # 这里一定要将candidates降序排列
        # for i in sorted(candidates, reverse=True):
        #     for j in range(i, target+1):
        #         if j == i:
        #             dp[j] = [[i]]
        #         else:
        #             dp[j].extend([x+[i] for x in dp[j-i]])
        # return dp[target]

        # 方法2：回溯+剪枝
        candidates.sort(reverse=True) # 从大到小排
        res = []
        pathes = []
        
        def findPath(nc: List[int], t: int):
            if t == 0:
                res.append(pathes[:]) # make a copy
                return
            limit = min(t, pathes[-1]) if pathes else t # 先选大数再选小数
            for num in nc:
                if num > limit:
                    continue
                pathes.append(num)
                findPath(nc, t - num)
                pathes.pop()

        findPath(candidates, target)
        return res


    
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7], 7))
    print(solution.combinationSum([2, 3, 5], 8))
