#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-07-02 08:15:14
@LastEditors: Thomas Young
@LastEditTime: 2020-07-02 13:20:14
'''
#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

# 示例：
# matrix = [
#     [1,  5,  9],
#     [10, 11, 13],
#     [12, 13, 15]
# ],
# k = 8,

# 返回 13。

# 提示：
# 你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。
#
from typing import List

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix) # 矩阵维度
        lb, ub = matrix[0][0], matrix[n - 1][n - 1] #值的上限、下限

        def countNumLE(num: int) -> int:
            cnt = 0
            row, col = 0, n - 1
            while 0 <= row < n and 0 <= col < n:
                while col >= 0 and matrix[row][col] > num:
                    col -= 1
                cnt += col + 1
                row += 1

            return cnt

        while lb < ub:
            mid = (lb + ub) >> 1
            cnt = countNumLE(mid)

            if cnt < k:
                lb = mid + 1
            elif cnt >= k:
                ub = mid
        return lb
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.kthSmallest([
        [1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ], 8))
