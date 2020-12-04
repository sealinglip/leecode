#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-27 09:48:47
LastEditors: Thomas Young
LastEditTime: 2020-11-28 22:12:15
'''
#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#
# 给定四个包含整数的数组列表 A, B, C, D, 计算有多少个元组(i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
# 为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 - 228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

# 例如:

# 输入:
# A = [1, 2]
# B = [-2, -1]
# C = [-1, 2]
# D = [0, 2]
# 输出:
# 2

# 解释:
# 两个元组如下:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

from typing import List
# @lc code=start
from collections import defaultdict
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # 将A、B归为一组，C、D归为一组
        key1 = defaultdict(int)
        for a in A:
            for b in B:
                k = a + b
                key1[k] = key1[k] + 1
        
        key2 = defaultdict(int)
        for c in C:
            for d in D:
                k = c + d
                key2[k] = key2[k] + 1

        cnt = 0
        for k in key1:
            if -k in key2:
                cnt += key1[k] * key2[-k]

        return cnt
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))