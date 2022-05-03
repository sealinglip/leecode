#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-07 08:05:58
LastEditors: Thomas Young
LastEditTime: 2020-11-07 18:05:18
'''
#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#
# 给定一个整数数组 nums，返回区间和在[lower, upper] 之间的个数，包含 lower 和 upper。
# 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j(i ≤ j)。

# 说明:
# 最直观的算法复杂度是 O(n^2) ，请在此基础上优化你的算法。

# 示例:
# 输入: nums = [-2, 5, -1], lower = -2, upper = 2,
# 输出: 3
# 解释: 3个区间分别是: [0, 0], [2, 2], [0, 2]，它们表示的和分别为: -2, -1, 2。

# Hard

from typing import List
# @lc code=start


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums:
            return 0

        # 记A(i + 1) = sum(nums[0], ……, nums[i])，A(0) = 0
        # 则S(i, j) = A(j + 1) - A(i)
        A = [0]
        for i, num in enumerate(nums):
            A.append(A[-1] + num)

        def countRangeSumInner(left: int, right: int) -> int:
            if left == right:
                return 0
            else:
                mid = (left + right) >> 1

                n1 = countRangeSumInner(left, mid)  # 左半区内部符合条件的区间数
                n2 = countRangeSumInner(mid + 1, right)  # 右半区内部符合条件的区间数
                ret = n1 + n2

                # 再加上左半区的起点和右半区的终点组成的符合条件的区间数(此时左右半区各自有序)
                i = left
                l = r = mid + 1
                # 计算每一个左半区的点能和右半区组成的区间数
                while i <= mid:
                    while l <= right and (A[l] - A[i]) < lower:
                        l += 1
                    while r <= right and (A[r] - A[i]) <= upper:
                        r += 1
                    ret += r - l
                    i += 1

                # 合并左右半区成有序数组，供上一级调用
                p1 = left
                p2 = mid + 1
                sorted = []
                while p1 <= mid or p2 <= right:
                    if p1 > mid:
                        sorted.append(A[p2])
                        p2 += 1
                    elif p2 > right or A[p1] < A[p2]:
                        sorted.append(A[p1])
                        p1 += 1
                    else:
                        sorted.append(A[p2])
                        p2 += 1

                for i, num in enumerate(sorted):
                    A[left + i] = sorted[i]

                return ret

        return countRangeSumInner(0, len(A) - 1)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countRangeSum([-2, 5, -1], -2, 2))
