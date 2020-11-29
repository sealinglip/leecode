#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-22 22:32:43
LastEditors: Thomas Young
LastEditTime: 2020-09-10 09:12:34
'''
#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。

# 说明：
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。

# 示例 1:
# 输入: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8,
# 所求解集为:
# [
#     [1, 7],
#     [1, 2, 5],
#     [2, 6],
#     [1, 1, 6]
# ]

# 示例 2:
# 输入: candidates = [2, 5, 2, 1, 2], target = 5,
# 所求解集为:
# [
#     [1, 2, 2],
#     [5]
# ]

from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 回溯+剪枝
        c = Counter(candidates)
        ncs = list(c.keys())
        ncs.sort(reverse=True) # 从大到小排
        cnt = [c[num] for num in ncs]
        res = []
        pathes = []

        def findPath(nc: List[int], t: int, start: int):
            if t == 0:
                res.append(pathes[:])  # make a copy
                return
            limit = min(t, pathes[-1]) if pathes else t # 从大往小找
            for i in range(start, len(ncs)):
                num = ncs[i]
                if num > limit or cnt[i] == 0:
                    continue
                pathes.append(num)
                cnt[i] -= 1
                findPath(nc, t - num, i)
                cnt[i] += 1
                pathes.pop()

        findPath(ncs, target, 0)
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum2([4, 4, 2, 1, 4, 2, 2, 1, 3], 6))
    print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(solution.combinationSum2([2, 5, 2, 1, 2], 5))
