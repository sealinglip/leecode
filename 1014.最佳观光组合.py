#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-17 09:34:44
@LastEditors: Thomas Young
@LastEditTime: 2020-06-17 10:09:02
'''
#
# @lc app=leetcode.cn id=1014 lang=python3
#
# [1014] 最佳观光组合
#
# 给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
# 一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）
# ：景点的评分之和减去它们两者之间的距离。
# 返回一对观光景点能取得的最高分。


# 示例：
# 输入：[8, 1, 5, 2, 6]
# 输出：11
# 解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

# 提示：
# 2 <= A.length <= 50000
# 1 <= A[i] <= 1000

from typing import List

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # score(i, j) = A[i] + i + A[j] - j (其中 i < j)
        # maxScore = max(A[i] + i) + max(A[j] - j)
        maxI = A[0] # 初始值
        maxScore = 0
        for j in range(1, len(A)):
            score = A[j] - j + maxI
            if score > maxScore:
                maxScore = score
            if A[j] + j > maxI:
                maxI = A[j] + j

        return maxScore

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
