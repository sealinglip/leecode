#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-04 10:10:03
LastEditors: Thomas Young
LastEditTime: 2020-09-04 10:17:26
'''
#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# 给出一个区间的集合，请合并所有重叠的区间。

# 示例 1:
# 输入: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# 输出: [[1, 6], [8, 10], [15, 18]]
# 解释: 区间[1, 3] 和[2, 6] 重叠, 将它们合并为[1, 6].

# 示例 2:
# 输入: intervals = [[1, 4], [4, 5]]
# 输出: [[1, 5]]
# 解释: 区间[1, 4] 和[4, 5] 可被视为重叠区间。

# 提示：
# intervals[i][0] <= intervals[i][1]

from typing import List
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort(key=lambda interval: interval[0])
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                last = res[-1]
                if interval[0] <= last[1] < interval[1]:
                    last[1] = interval[1]
                elif last[1] < interval[0]:
                    res.append(interval)
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(solution.merge([[1, 4], [4, 5]]))
