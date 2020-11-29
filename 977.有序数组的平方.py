#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-16 08:52:53
LastEditors: Thomas Young
LastEditTime: 2020-10-16 09:17:55
'''
#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

# 示例 1：
# 输入：[-4, -1, 0, 3, 10]
# 输出：[0, 1, 9, 16, 100]

# 示例 2：
# 输入：[-7, -3, 2, 3, 11]
# 输出：[4, 9, 9, 49, 121]

# 提示：
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A 已按非递减顺序排序。

from typing import List
# @lc code=start
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return A
        
        if A[0] < 0: # 有负数
            if A[-1] <= 0:
                A.reverse()  # reverse
            else:
                A = [abs(a) for a in A]
                A.sort()

        return [a * a for a in A]
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortedSquares([-4, -1, 0, 3, 10]))
    print(solution.sortedSquares([-7, -3, 2, 3, 11]))
