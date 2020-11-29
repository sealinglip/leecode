#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-20 21:12:44
LastEditors: Thomas Young
LastEditTime: 2020-09-20 21:29:54
'''
#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。

# 示例 1:
# 输入:
# matrix = [
#     [1,   3,  5,  7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 50]
# ]
# target = 3
# 输出: true

# 示例 2:
# 输入:
# matrix = [
#     [1,   3,  5,  7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 50]
# ]
# target = 13
# 输出: false

from typing import List
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        # copy from java.util.Arrays#binarySearch(int[], int, int, int)
        def binarySearch(arr: List[int], fromIndex: int, toIndex: int, key: int) -> int:
            low, high = fromIndex, toIndex - 1

            while low <= high:
                mid = (low + high) >> 1
                midVal = arr[mid]

                if midVal < key:
                    low = mid + 1
                elif midVal > key:
                    high = mid - 1
                else:
                    return mid
            
            return -(low + 1)

        # 变相的折半查找
        N, M = len(matrix), len(matrix[0])
        rowEnd = [matrix[row][-1] for row in range(N)]
        idx = binarySearch(rowEnd, 0, N, target)
        if idx >= 0:
            return True
        else: # 转换为可能存在该值的行序号
            row = -idx - 1
            if row >= N:
                return False
            idx = binarySearch(matrix[row], 0, M, target)
            return idx >= 0

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchMatrix([
        [1, 1],
    ], 3))
    print(solution.searchMatrix([
        [1],
    ], 3))
    print(solution.searchMatrix([
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 3))
    print(solution.searchMatrix([
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 13))
