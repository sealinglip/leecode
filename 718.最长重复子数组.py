#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-07-01 10:21:50
@LastEditors: Thomas Young
@LastEditTime: 2020-07-01 13:58:51
'''
#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

# 示例 1:

# 输入:
# A: [1, 2, 3, 2, 1]
# B: [3, 2, 1, 4, 7]
# 输出: 3
# 解释:
# 长度最长的公共子数组是[3, 2, 1]。
# 说明:

# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100

from typing import List
# @lc code=start
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return 0
        
        a_len, b_len, max_len = len(A), len(B), 0

        # 方法1：典型的动态规划
        # 如果用dp[i][j]表示当A的第i-1个字符和B的第j-1个字符对齐时，当前对齐位置（含）总共匹配的前缀字符数
        # 则有 dp[i][j] = dp[i - 1][j - 1] + 1 if A[i - 1] == B[j - 1] else 0
        # 其中 0 < i <= a_len, 0 < j <= b_len， dp[0][*] = dp[*][0] = 0
        # 由于 dp[i][j]只依赖于dp[i - 1][j - 1]，所以可以将dp简化为一维数据
        # dp[j] 代表第i轮循环时当A的第i-1个字符和B的第j-1个字符对齐时，当前对齐位置（含）总共匹配的前缀字符数
        # dp = [0 for i in range(b_len + 1)] # 长度为B数组长度+1
        # for i in range(1, a_len + 1):
        #     for j in range(b_len, 0, -1):
        #         if A[i - 1] == B[j - 1]:
        #             dp[j] = dp[j - 1] + 1
        #         else:
        #             dp[j] = 0
        #         max_len = max(max_len, dp[j])

        # 方法2：移动窗口
        # 依次将A的第0个字符和B的第b_len-1个字符对齐，A往前移，直至A的第a_len-1个字符和B的第0个字符对齐
        # 每次对齐，都求出重叠部分里最大相同子串的长度
        total = a_len + b_len - 1 # 总共要对齐比较的次数
        for i in range(total):
            # A B 重叠部分跟i的关系是 A的区间为[i, a_len + i)，B的区间为[a_len - 1, a_len + b_len - 1)
            # 重叠部分长度为 min(a_len + b_len, a_len + i + 1) - max(i, a_len - 1)
            s = max(i, a_len - 1)
            overlap = min(a_len + b_len - 1, a_len + i) - s
            a_s, b_s = s - i, s - a_len + 1 #重叠部分在A，B中分别的起始索引
            k = 0 # 公共子数组长度
            for j in range(overlap):
                if A[a_s + j] == B[b_s + j]:
                    k += 1
                else:
                    k = 0
                max_len = max(max_len, k)

        return max_len

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
