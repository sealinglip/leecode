#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-25 09:54:39
LastEditors: Thomas Young
LastEditTime: 2020-10-25 22:09:20
'''
#
# @lc app=leetcode.cn id=845 lang=python3
#
# [845] 数组中的最长山脉
#
# 我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：

# B.length >= 3
# 存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# （注意：B 可以是 A 的任意子数组，包括整个数组 A。）
# 给出一个整数数组 A，返回最长 “山脉” 的长度。
# 如果不含有 “山脉” 则返回 0。

# 示例 1：
# 输入：[2, 1, 4, 7, 3, 2, 5]
# 输出：5
# 解释：最长的 “山脉” 是[1, 4, 7, 3, 2]，长度为 5。

# 示例 2：
# 输入：[2, 2, 2]
# 输出：0
# 解释：不含 “山脉”。

# 提示：
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000

from typing import List
# @lc code=start
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        maxSpan = 0
        if A and len(A) >= 3:
            # left, peak记录山脉的左边界、山顶
            left = peak = None
            
            for i in range(1, len(A) - 1):
                lTrend = 1 if A[i] > A[i-1] else (0 if A[i] == A[i-1] else -1)
                rTrend = 1 if A[i+1] > A[i] else (0 if A[i+1] == A[i] else -1)
                if lTrend == 1:
                    if left is None:
                        left = i - 1
                    if rTrend == -1:
                        peak = i
                elif lTrend == 0:
                    left = peak = None
                else:
                    if rTrend != -1:
                        if left is not None and peak is not None:
                            maxSpan = max(maxSpan, i - left + 1)
                        left = peak = None
            if left is not None and peak is not None:
                maxSpan = max(maxSpan, len(A) - left)
            
        return maxSpan

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestMountain([0, 0, 1, 0, 0, 1, 1, 1, 1, 1]))
    print(solution.longestMountain([40, 51, 29, 19, 50, 25]))
    print(solution.longestMountain([0, 1, 0, 1]))
    print(solution.longestMountain([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(solution.longestMountain([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]))
    print(solution.longestMountain([0, 1, 2, 2, 3, 4, 5, 4, 3, 2, 1, 0]))
    print(solution.longestMountain([2, 1, 4, 7, 3, 2, 5]))
    print(solution.longestMountain([2, 2, 2]))
    print(solution.longestMountain([0, 2, 2]))
