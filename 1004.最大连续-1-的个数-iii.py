#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-02-19 21:28:36
LastEditors: Thomas Young
LastEditTime: 2021-02-19 21:59:02
'''
#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
# 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
# 返回仅包含 1 的最长（连续）子数组的长度。

# 示例 1：
# 输入：A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K = 2
# 输出：6
# 解释：
# [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。

# 示例 2：
# 输入：A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K = 3
# 输出：10
# 解释：
# [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。

# 提示：
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] 为 0 或 1

from typing import List
# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # 滑动窗口
        N = len(A)
        l = r = 0
        longest = 0

        # 下面保证[l, r)区间内的0个数不超过起始值K，记录区间的最大跨度
        # 当K递减到0时，[l, r)区间内的0个数恰好为起始值K
        while r < N:
            if A[r] == 0:
                if K == 0:
                    while A[l]:
                        l += 1
                    l += 1
                else:
                    K -= 1
            r += 1
            longest = max(longest, r - l)
        
        return longest
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
    print(solution.longestOnes(
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
