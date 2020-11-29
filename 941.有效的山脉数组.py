#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-03 07:53:42
LastEditors: Thomas Young
LastEditTime: 2020-11-03 08:02:57
'''
#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#
# 给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

# 让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

# A.length >= 3
# 在 0 < i < A.length - 1 条件下，存在 i 使得：
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]

# 示例 1：
# 输入：[2, 1]
# 输出：false

# 示例 2：
# 输入：[3, 5, 5]
# 输出：false

# 示例 3：
# 输入：[0, 3, 2, 1]
# 输出：true

# 提示：
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000

from typing import List
# @lc code=start
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if not A or len(A) < 3 or A[1] <= A[0]:
            return False

        asc = True
        for i in range(2, len(A)):
            if A[i] == A[i - 1]:
                return False
            elif asc:
                if A[i] < A[i - 1]:
                    asc = False
            else:
                if A[i] > A[i - 1]:
                    return False

        return asc == False


        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.validMountainArray([0, 1, 2, 3, 4]))
    print(solution.validMountainArray([0, 1, 2, 3, 4, 4, 3]))
    print(solution.validMountainArray([0, 1, 2, 3, 4, 2, 3]))
    print(solution.validMountainArray([0, 1, 2, 3, 4, 3, 2]))
